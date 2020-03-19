#!/usr/bin/env python3

#---------------------------------
import sys
import datetime
import setup
#---------------------------------
def printInitializationMessage():
	print('TBOT: (Trading Bot)')
	print('Starting at: <datetime>')
	print('Config file: /path/to/config.ini')
	print('Coin per: <coin-per>')
	print('Strategy: <straategy>')
	print('===============')
	print('tbot Execution BEGIN')
	print('===============')

def printFinalizationMessage():
	print('===============')
	print('tbot Execution END')
	print('===============')

def userPressCtrC():
	return False

def getPrice():
	print("<datetime> <coin-per>: <price>")


#-------Main----------------------
if __name__ == '__main__':	
	configuration = setup.Configuration()
	configResult = configuration.load()
	if not configResult:
		print('ERROR: Wrong configuration.')
		exit(1)
	print("Configuration loaded.")
		
	# paramVerbose = true
	# printInitializationMessage()

	# broker = BrokerFactory(configuration)
	# strategy = StretegyFactory(configuration)
	# logger = Logger(configuration, paramVerbose)

	# while (userPressCtrC()):
	# 	price = broke.getPrice()
	# 	logger.log(configuration.getPer() + "Price: "+str(price))

	# printFinalizationMessage()
