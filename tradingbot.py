import setup
import time
import requests

class TBot:

	configuration = None

	def start(self):
		config = setup.Configuration()
		configResult = config.load()
		if not configResult:
			print('ERROR: Wrong configuration.')
			exit(1)
		self.configuration = config
		print(config.getConfigOutput())
		
		while True:
			self.waitTime()
			self.queryPrice()

		exit(0)

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