import setup
import time
import requests

class TBot:

	configuration = None

	stateProcessing = "processing"
	stateOperating = "operating"
	stateObserving = "observing"
	stateClosing = "closing"
	stateFinal = "final"
	stateError = "error"

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


	def actionStateProcessing(self, state):
		return self.stateOperating
	
	def actionStateOperating(self, state):
		return self.stateObserving

	def actionStateObserving(self, state):
		return self.stateClosing

	def actionStateClosing(self, state):
		return self.stateProcessing

	def actionStateError(self, state):
		return self.stateFinal
		
	def actionStateFinal(self):
		print("Trading activity stopped.")