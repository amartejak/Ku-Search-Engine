import os
from collections import defaultdict
import pickle

dict_pf=set()
post_pf={}
post_pf=defaultdict(dict)

def main():
	path,dirs,files = next(os.walk("clean_docs/"))
	keys_pf = []
	for i in range(0, len(files)):
		keys_pf.append(i)
	allDocsPf = {}

	for i in range(0, len(files)):
		(k,v)=(keys_pf[i], "clean_docs/"+files[i])
		allDocsPf[k] = v
	print("Nothing")
	assignDict(allDocsPf)
	if not os.path.exists('Saved_pickle_files'):
		os.makedirs('Saved_pickle_files')          
	file_a = open(r'Saved_pickle_files/dict.pkl', 'wb')
	pickle.dump(dict_pf, file_a)
	file_a.close()
	# print(dict_pf)

	#Store post_pf in pickle file
	file_b = open(r"Saved_pickle_files/post_pf.pkl", "wb")
	pickle.dump(post_pf, file_b)
	file_b.close()
	#print(post_pf)
	
	#Store list of docs in pickle file
	file_c= open(r"Saved_pickle_files/allDocsPf.pkl", "wb")
	pickle.dump(allDocsPf, file_c)
	file_c.close()
	#print(allDocsPf)
	
	#Store the keys_pf in pickle file
	file_d = open(r"Saved_pickle_files/keys_pf.pkl", "wb")
	pickle.dump(keys_pf, file_d)
	file_d.close()
	#print(keys_pf)

def assignDict(allDocsPf):
	global dict_pf, post_pf
	for id_doc in allDocsPf:
		#Opening the pickle file
		#print(allDocsPf[id_doc])
		f = open(allDocsPf[id_doc], 'r', encoding="utf8")
		docWhole = f.read()
		#print(docWhole)
		f.close()
		docWhole = docWhole.split()
		#Set creates a set of tokens in the documents
		unique_terms_doc = set(docWhole)
		#print(unique_terms_doc)
		#So, in the previous created dict_pf, I'm adding all these terms
		dict_pf = dict_pf.union(unique_terms_doc)
		#print(dict_pf)
		# Now we'll set the post_pf, with the values equal to the frequency of terms in the document
		for terms in unique_terms_doc:
			post_pf[terms][id_doc] = docWhole.count(terms)
