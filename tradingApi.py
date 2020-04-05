import setup

class TradingApi:
	"""Base class for the trading every API.
	"""
	def __init__(self):
		print("TadingApi created.")


class CoinsbitApi(TradingApi):
	"""Trading API for www.coinsbit.io
	This trading API is based on REST services.
	"""
	def __init__(self):
		print("CoinsbitApi created.")


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
		
		platform = botConfiguration.getPlatform()
		if not platform or not platform in self.definedApis.keys():
			return False

		api = self.definedApis[platform]()
		return api