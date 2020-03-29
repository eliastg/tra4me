import setup
import vectortrend

class TradingAPIFactory:

	definedStrategies = [
		'vectortrend': vectortrend.VectorTrend
	]

	def getStrategy(self, configuration):
		strategyName = configuration.getStrategy()

		if not strategyName in self.definedStrategies:
			print("Error: The selected strategy is not defined. Check the configuration file.")
			return False
		
		return self.definedStrategies[strategyName]()