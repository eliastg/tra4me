import setup

class TradingApi:
	"""Base class for the trading every API.
	"""
	def __init__(self):
		print("TadingApi created.")

	def nextPrice(self):
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
	def __init__(self):
		print("CsvApi created")

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
			return CsvApi()

		platform = botConfiguration.getPlatform()
		if not platform or not platform in self.definedApis.keys():
			return False

		api = self.definedApis[platform]()
		return api