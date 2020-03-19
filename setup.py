import sys
import configparser

class Configuration:
	argVerbose = '--verbose'
	argQuiet = '--quite'
	argConfig = '--config'
	argHelp = '--help'

	arguments = {
		argVerbose: True,
		argQuiet: False,
		argConfig: 'config.ini',
		argHelp: False
	}

	def parseArguments(self):
		if len(sys.argv) < 2:
			return False

		boolArgs = [self.argHelp, self.argQuiet, self.argVerbose]
		for a in boolArgs:
			if a in sys.argv:
				self.arguments[a] = True

		return True

	def checkFileSintaxys(self):
		# For now
		return True

	def load(self):
		if not self.parseArguments():
			print("WARNING: Missing arguments. Default configuration will be loaded.")

		file = configparser.ConfigParser()
		readList = file.read(self.arguments[self.argConfig])
		if len(readList) != 1:
			print("ERROR: The configuration file cannot be read.")
			return False
		self.configFile = file
		return self.checkFileSintaxys()