import sys
import configparser
import datetime
import time

class Configuration:
	configFilePath = ''
	configFileIni = None

	argVerbose = '--verbose'
	argQuiet = '--quite'
	# argConfig = '--config'
	argHelp = '--help'

	arguments = {
		argVerbose: True,
		argQuiet: False,
		# argConfig: 'config.ini',
		argHelp: False
	}

	def parseArguments(self):
		if len(sys.argv) < 2:
			return False
		boolArgs = [self.argHelp, self.argQuiet, self.argVerbose]
		for a in sys.argv:
			if a == sys.argv[0]:
				continue
			if a in boolArgs:
				self.arguments[a] = True
			else:
				self.configFilePath = a
		
		return (self.configFilePath != '')

	def checkFileSintaxys(self):
		# For now
		return True

	def load(self):
		if not self.parseArguments():
			print("WARNING: Missing arguments. Default configuration will be loaded.")
			return False

		file = configparser.ConfigParser()
		readList = file.read(self.configFilePath)
		if len(readList) != 1:
			print("ERROR: The configuration file cannot be read.")
			return False
		self.configFileIni = file
		return self.checkFileSintaxys()

	def getConfigOutput(self):
		# Trading Bot (tbot)
		# Starting at: <datetime>
		# Config file: /path/to/config.ini
		# Coin per: <coin-per>
		# Strategy: <straategy>
		endl = '\r\n'
		baseSection = self.configFileIni['base']
		tradingSection = self.configFileIni['trading']
		dtnow = datetime.datetime.fromtimestamp(time.time())

		out = '__________________________'+endl
		out += "Trading Bot (tbot)"+endl
		out += "Start date-time: "+"{}/{}/{} {}:{}:{}".format(
			dtnow.year,dtnow.month,dtnow.day,
			dtnow.hour,dtnow.minute,dtnow.second
		)+endl
		out += "Configuration file: "+self.configFilePath+endl
		out += "Coin per: "+tradingSection['coinper']+endl
		out += "Strategy: "+tradingSection['strategy']+endl
		out += '_________________________'+endl
		return out
