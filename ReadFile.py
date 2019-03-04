def getFileContents(filePath):
	f=open(filePath, "r")
	lines = f.readlines()
	contents = ''.join(lines)
	return contents, lines	