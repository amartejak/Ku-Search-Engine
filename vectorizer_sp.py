import pickle
from collections import defaultdict
import math
from query_pre_processing import removeTagsQuery
from functools import reduce
import sys


file2 = open(r'Pre_Processing/Saved_pickle_files/dict.pkl', 'rb')
tokens_list_word = pickle.load(file2)
file2.close()
file3 = open(r'Pre_Processing/Saved_pickle_files/post_pf.pkl', 'rb')
posting_dict = pickle.load(file3)
file3.close()

file4 = open(r'Pre_Processing/Saved_pickle_files/allDocsPf.pkl', 'rb')
all_doc_dicts = pickle.load(file4)
file3.close()

frequency = defaultdict(int)

inverseFreq_value = 0

eucLen = defaultdict(float)


total_len_docs = len(all_doc_dicts)

def main_func(query):
	termLengthToFreq()
	eucLength_docs()
	enterQueryUser(query)

def termLengthToFreq():
	global frequency
	for tokens in tokens_list_word:
		frequency[tokens] = len(posting_dict[tokens])

def inverseFreq(tokens):
	if tokens in tokens_list_word:
		global inverseFreq_value
		inverseFreq_value = math.log10(total_len_docs/frequency[tokens])
		return inverseFreq_value
	else:
		return inverseFreq_value

def weight(tokens, i):
	if i in posting_dict[tokens]:
		return posting_dict[tokens][i]*inverseFreq(tokens)
	else:
		return 0

def eucLength_docs():
	global eucLen 
	for i in all_doc_dicts:
		length_tokens = 0
		for tokens in tokens_list_word:
			length_tokens  = length_tokens  + (weight(tokens,i)**2)
		eucLen[i] = math.sqrt(length_tokens )

def enterQueryUser(query):
	search_que= query
	if search_que== "":
		sys.exit()
	
	search_que= removeTagsQuery(search_que)
	search_que= list(filter(('p').__ne__, search_que))
	match_query = []
	for terms in search_que:
		match_query.append(set(posting_dict[terms].keys()))
	match_query = list(filter((set()).__ne__, match_query))
	try:
		re_sub = reduce(set.intersection, [x for x in match_query])
	except:
		re_sub = 0
	scoresQuery = []
	if not re_sub:
		print("DOcument not found")
	else:
		for id in re_sub:
			cosineSimilarityScore = 0
			for term in search_que:
				if term in tokens_list_word:
					cosineSimilarityScore += inverseFreq(term)*weight(term,id)
			cosineSimilarityScore /=eucLen[id]
			scoresQuery.append([id, cosineSimilarityScore])
		scoresQuery = list(map(tuple, scoresQuery))
		scoresQuery = sorted(scoresQuery, key=lambda tup: tup[1], reverse=True)

		print("Score: filename")
		get_res = []
		result_dict = {}
		for (x,rates) in scoresQuery:
			get_res.append(str(rates)+": "+ all_doc_dicts[x])
			result_dict[all_doc_dicts[x]] = rates
		new_resdict = {}
		for i in result_dict.keys():
			f= open('Pre_Processing/'+(i) , 'rt')
			c = 0
			k = ''
			for line in f:
				if(c==0):
					c=c+1
					k=line.replace('\n','')
			new_resdict[k]= result_dict[i]
		print(new_resdict)
		file_a = open(r'Pre_Processing/Saved_pickle_files/result_dict.pkl', 'wb')
		pickle.dump(new_resdict, file_a)
		file_a.close()

if __name__ == "__main__":
	main_func('admissions')