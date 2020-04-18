import setup
import datetime

class TradingApi:
	"""Base class for the trading every API.
	"""

	configuration = None

	def __init__(self, botConfiguration):
		if not botConfiguration:
			raise Exception('No valid configuration object to create TradingApi')
		self.configuration = botConfiguration
		print("TadingApi created.")

	def getPrice(self):
		return 0.0


class CoinsbitApi(TradingApi):
	"""Trading API for www.coinsbit.io
	This trading API is based on REST services.
	"""
	def __init__(self):
		print("CoinsbitApi created.")

class CsvApi(TradingApi):
	"""Reads from a CSV test data file instead of consume a real API.
	This class is meant for Back Testing purposes. 
	"""
	
	_testFile = None
	
	def __init__(self, botConfiguration):
		TradingApi.__init__(self, botConfiguration)
		self._testFile = open(self.configuration.getTestFilePath(), 'r')
		print("CsvApi created")

	def __del__(self):
		if self._testFile:
			self._testFile.close()
	
	def getPrice(self):
		if not self._testFile:
			raise Exception('No access to test file')
		
		line = self._testFile.readline()
		if not line:
			return False
		
		line = line.split(',')
		if not line or len(line) != 2:
			raise Exception('Unexpected syntax in test file.')

		time = self.filterDateTime(line[0])
		price = self.filterPrice(line[1])
		return (time, price)

	def filterDateTime(self, datetimeStr):
		try:
			return datetime.datetime.strptime(datetimeStr, '%Y-%m-%d %H:%M:%S')
		except Exception as e:
			raise Exception("Invalid syntax in datatime value, in the test file. Expected: 0000-00-00- 00:00:00")

	def filterPrice(self, floatStr):
		if type(floatStr) != str or len(floatStr) < 1:
			raise Exception('Invalid syntax in price value, in the test file.')

		l = len(floatStr)
		if floatStr[l-1] == '\n':
			return floatStr[:l-1]


class TradingAPIFactory:
	"""Creates trading API's from setup.Configuration object.
	"""
	
	definedApis = {
		'coinsbit.io': CoinsbitApi
	}

	def getApi(self, botConfiguration):
		"""Creates a TradingApi instance that corresponds to the bot configuration.
		
		Arguments:
			botConfiguration {setup.Configuration} -- The bot configuration.
		
		Returns:
			TradingApi -- A trading API object that that corresponds to the bot configuration.
			Bool -- Returns False if the trading API configuration is not defined.
		"""
		
		if not botConfiguration:
			return False
		
		if botConfiguration.isTest():
			return CsvApi(botConfiguration)

		platform = botConfiguration.getPlatform()
		if not platform or not platform in self.definedApis.keys():
			return False

		api = self.definedApis[platform](botConfiguration)
		return api