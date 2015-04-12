import gensim
import math
import nltk
import json
from gensim import corpora,models,similarities
abstracts={}

with open("abstract_clean.json",'r') as f:
	abstracts=json.load(f)


i=0
indices=[i for i in abstracts]
stoplist=nltk.corpus.stopwords.words("english") + ['.','\\','.',',','?',')','(','[',']','{','}']
dictionary=corpora.Dictionary(line.lower().split() for line in [abstracts[i]["content"] for i in indices])
stop_ids = [dictionary.token2id[stopword] for stopword in stoplist if stopword in dictionary.token2id]
dictionary.filter_tokens(stop_ids)
dictionary.compactify()
print(dictionary)
dictionary.save('abstracts.dict')
id2word = gensim.corpora.Dictionary.load('abstracts.dict')
my_corpus = [dictionary.doc2bow(line.lower().split()) for line in [abstracts[i]["content"] for i in indices]] 
corpora.MmCorpus.serialize('abstracts.mm', my_corpus) #CHANGE HERE
