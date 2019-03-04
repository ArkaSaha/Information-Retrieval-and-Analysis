import re
import itertools

def generateTokens(contents,filePath):
	tokens = re.sub(r"[^a-zA-Z0-9\s]|[\x00-\x08\x0b-\x1f\x7f-\xff]+",'',contents)
	tokens = re.sub(r"\b\w{,1}\b",'', tokens).lower().split()
	return list(zip(tokens, itertools.repeat(filePath)))

## To run in stand alone mode
#contents = "Hey, U.S.A Jonathan S \x0cyou - what a are\nyou's   doing	here!? 05/90.5903"
#filePath = "10.txt"
#tokens = re.sub(r"[^a-zA-Z0-9\s]|[\x00-\x08\x0b-\x1f\x7f-\xff]+",'',contents)
#tokens = re.sub(r"\b\w{,1}\b",'', tokens).lower().split()
#docIDindex = list(range(1, len(tokens)+1))
#output = generateTokens(contents,filePath)
#print(contents)
#print(tokens)
#print("\n")
#print(output)