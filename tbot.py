#!/usr/bin/env python3

#---------------------------------
import sys
import datetime
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
	
	printInitializationMessage()

	while (userPressCtrC()):
		price = getPrice()
	
	printFinalizationMessage()
