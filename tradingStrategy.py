import setup


class TradingStrategy:
	"""Base class of the trading strategies.
	"""
	def __init__(self):
		print("TradingStratedy created.")

class VectorTrend(TradingStrategy):
	"""This is a strategy that uses vectors and naive analytics to detect a trend.
	This strategy was created by Elías Trenard García with development purposes,
	it is not a valid strategy. Used under your own responsability.
	"""
	def __init__(self):
		print("VectorsTrend strategy created.")



class TradingStrategyFactory:
	"""Creates trading strategies from setup.Configuration object.
	"""

	definedStrategies = {
		'vectorTrend': VectorTrend
	}

	def getStrategy(self, botConfiguration):
		"""Returns a strategy object for the corresponding configuration, if configuration is correct.
		It will return False otherwise, in case of error or undefined configuration.

		Arguments:
			botConfiguration setup.Configuration -- The configuration object.
				
		Returns:
			TradingStrategy -- A trading strategy that corresponds to the configuration file.
		"""
		if not botConfiguration: 
			return False
		
		strategy = botConfiguration.getStrategy()
		
		if not strategy or not strategy in self.definedStrategies.keys():
			return False
		
		strategy = self.definedStrategies[strategy]()
		return strategy