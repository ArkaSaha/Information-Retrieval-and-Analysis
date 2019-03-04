from nltk.stem.porter import *
from nltk.stem.snowball import SnowballStemmer

portStemmer = PorterStemmer()
snowStemmer = SnowballStemmer("english")

def docPortStem(tokenPair):
	return [(portStemmer.stem(token),docID) for token, docID in tokenPair]

def docSnowStem(tokenPair):
	return [(snowStemmer.stem(token),docID) for token, docID in tokenPair]