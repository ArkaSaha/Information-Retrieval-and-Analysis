from DirListing import listFiles 
from ReadFile import getFileContents
from Tokenizer import generateTokens
from Stemmer import docPortStem,docSnowStem
import CONST


fileList = listFiles(CONST.rootDir)

## To loop over all the files
#for file in fileList[0:2]:
#	fileContent = getFileContents(file)[0]
#	tokenPair = generateTokens(fileContent,file)
#	stemTokenPair = docSnowStem(tokenPair)

## To run for a single file - first file in the directory
fileContent = getFileContents(fileList[0])[0]
print(fileContent)

tokenPair = generateTokens(fileContent,fileList[0])
print(tokenPair)

stemTokenPair = docSnowStem(tokenPair)
print(stemTokenPair)