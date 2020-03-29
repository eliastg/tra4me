import setup
import time
import requests
import tradingStrategy
import tradingApi

class TBot:

	configuration = None

	stateProcessing = "processing"
	stateOperating = "operating"
	stateObserving = "observing"
	stateClosing = "closing"
	stateFinal = "final"
	stateError = "error"

	strategy = None
	apiService = None
	operation = None

	def start(self):
		config = setup.Configuration()
		configResult = config.load()
		if not configResult:
			print('ERROR: Wrong configuration.')
			exit(1)
		self.configuration = config
		print(config.getConfigOutput())
		
		self.trade()

	def waitTime(self):
		time.sleep(1)

	def queryPrice(self):
		apiEndPoint = 'https://www.coinsbit.io/api/v1/public/ticker'
		response = requests.get(
			'https://www.coinsbit.io/api/v1/public/ticker', 
			{ 'market': 'BTC_USD' }
		).json()

		if(not response['success']):
			print(response['message'])
		else:
			print('BTC_USD: {}'.format(response['result']['last']))

	def trade(self):
		state = self.stateProcessing
		self.strategy = tradingStrategy.TradingStrategyFactory.getStrategy(self.configuration)
		self.apiService = tradingApi.TradingAPIFactory.getApi(self.configuration)

		while state != self.stateFinal:

			print("State: {}".format(state))
			self.waitTime()

			if state == self.stateProcessing:
				state = self.actionStateProcessing(state)
			
			elif state == self.stateOperating:
				state = self.actionStateOperating(state)

			elif state == self.stateObserving:
				state = self.actionStateObserving(state)

			elif state == self.stateClosing:
				state = self.actionStateClosing(state)

			elif state == self.stateError:
				state = self.actionStateError(state)
		
		self.actionStateFinal()

	def tradingWindowsOpen(self):
		return True

	def actionStateProcessing(self, state):
		try:
			if not self.tradingWindowsOpen():
				return self.stateFinal

			price = self.apiService.nextPrice()
			if not price:
				return self.stateProcessing
			
			self.operation = self.strategy.nextOperation(price)
			if not self.operation:
				return self.stateProcessing
		except:
			print("An exception ocurred in the Processing state.")
			return self.stateError

		return self.stateOperating
	
	def actionStateOperating(self, state):
		try:
			if not self.tradingWindowsOpen():
				return self.stateFinal

			if not self.operation:
				print("Mal function error: The Operating state has been reached without having a valid order.")
				return self.stateError

			if not self.operation.executed():
				self.operation.execute()
			
			if self.operation.executionConfirmed():
				return self.stateOperating

		except:
			print("An exception occurred in the Operating state.")
			return self.stateError

		return self.stateObserving

	def actionStateObserving(self, state):
		try:
			if if not self.tradingWindowsOpen():
				return self.stateFinal
			
			if not self.operation.reachedTP_SL():
				return self.stateObserving
		except:
			print("An exception occurred in the Observing state.")
			return self.stateError

		return self.stateClosing

	def actionStateClosing(self, state):
		try:
			if not self.tradingWindowsOpen():
				return self.stateFinal
			
			if not self.operation.closeRequested():
				self.operation.close()
			
			if not self.operation.closed():
				return self.stateClosing
		except:
			print("An exception occurred in the Closing state")
			return self.stateError
		
		self.balanceCheck()
		return self.stateProcessing

	def actionStateError(self, state):
		return self.stateFinal
		
	def actionStateFinal(self):
		print("Trading activity stopped.")