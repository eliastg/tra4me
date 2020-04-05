import sys
import configparser
import datetime
import time

class Configuration:
	configFilePath = ''
	csvTestFilePath = ''
	configFileIni = None

	argVerbose = '--verbose'
	argQuiet = '--quite'
	# argConfig = '--config'
	argHelp = '--help'
	argTestData = '--test-data' #--test-data /path/to/file.csv


	arguments = {
		argVerbose: True,
		argQuiet: False,
		# argConfig: 'config.ini',
		argHelp: False,
		argTestData: False
	}

	iniSectionTrading = 'trading'
	iniSectionBase = 'base'
	iniKeyStrategy = 'strategy'
	iniKeyPlatform = 'platform'

	def parseArguments(self):
		if len(sys.argv) < 2:
			return False
		boolArgs = [self.argHelp, self.argQuiet, self.argVerbose, self.argTestData]
		for a in sys.argv:
			if a == sys.argv[0]:
				continue
			if a in boolArgs:
				self.arguments[a] = True
			elif self.getExtension(a) == 'ini':
				self.configFilePath = a
			elif self.getExtension(a) == 'csv':
				self.csvTestFilePath = a
		
		return (self.configFilePath != '')

	def getExtension(self, a):
		if type(a) != str or len(a) < 5:
			return False
		return a[len(a)-3:]  

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

	def getStrategy(self):
		"""Returns the strategy from the configuration file.
		
		Returns:
			String -- The name of the strategy as it is in the configuration file.
			Bool -- It will return false if there is no strategy defined.
		"""
		if not self.configFileIni:
			return False
		return self.configFileIni[self.iniSectionTrading][self.iniKeyStrategy]

	def getPlatform(self):
		"""Returns the platform from the configuration file.
		
		Returns:
			String -- The name of the platform defined in the configuration file.
			Bool -- It will return False if there is no strategy defined.
		"""
		if not self.configFileIni:
			return False
		return self.configFileIni[self.iniSectionTrading][self.iniKeyPlatform]

	def isTest(self):
		return self.arguments[self.argTestData]

	def getTestFilePath(self):
		return self.csvTestFilePath