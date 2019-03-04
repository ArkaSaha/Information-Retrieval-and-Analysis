from os import listdir
from os.path import isfile, join

def listFiles(rootDir):
	onlyfiles = [join(rootDir, f) for f in listdir(rootDir) if isfile(join(rootDir, f))]
	return onlyfiles