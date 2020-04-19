import setup


class TradingStrategy:
	"""Base class of the trading strategies.
	"""
	def __init__(self):
		print("TradingStratedy created.")

	def nextOperation(self, price):
		return False

class MeanReversion(TradingStrategy):
	"""This strategy based on the existence of an average value for the price, 
	to which it can return to. The analytics uses a moving average approach.
	"""
	def __init__(self):
		print("MeanReversion strategy created.")



class TradingStrategyFactory:
	"""Creates trading strategies from setup.Configuration object.
	"""

	definedStrategies = {
		"mean-reversion": MeanReversion
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
		
		return self.definedStrategies[strategy]()