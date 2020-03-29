class TradeOperation:
	def __init__(self, configuration):
		print("Trade Operation Created")

class BuyOperation(TradeOperation):
	def __init__(self, configuration):
		print("Buy operation created.")

class SellOperation(TradeOperation):
	def __init__(self, configuration):
		print("Sell operation created.")
