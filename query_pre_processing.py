import os
import re
import string
from lxml import html
from lxml.html.clean import clean_html
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

TAG_RE_Pattern = re.compile(r'<[^>]+>')

#To remove the stop words
stop_words = set(stopwords.words('english'))

def puns(ch):
    if ch.isalpha():
        return ch
    else:
        return ' '

def removeDuplicates(input):
	#split input string separated by space
	input = input.split(" ")
	#joins two adjacent elements in iterable way
	for i in range(0, len(input)):
		input[i] = "".join(input[i])
	# now create dictionary using counter method which will have strings as key and their frequencies as value
	UniqW = Counter(input)
	#joins two adjacent elements in an iterable way
	s = " ".join(UniqW.keys())
	return s

def removeTagsQuery(readFileQuery):
	readFileQuery = clean_html(readFileQuery)
	readFileQuery = ''.join(puns(ch)for ch in readFileQuery)
	readFileQuery = ' '.join(readFileQuery.split())
	removeTagsVar = TAG_RE_Pattern.sub('', readFileQuery)
	removeTagsVar = re.sub('<script>.*?</script>', '', removeTagsVar)
	lowerVar = readFileQuery.lower()
	lowerVar = removeDuplicates(lowerVar)
	words_tokens = word_tokenize(lowerVar)
	filteredSentence = [w for w in words_tokens if not w in stop_words]
	filteredSentence = []
	for w in words_tokens:
		if w not in stop_words:
			filteredSentence.append(w)
	#print(filteredSentence)
	return filteredSentence