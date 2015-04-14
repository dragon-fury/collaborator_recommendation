import gensim, math, re, json, ast, nltk
from nltk.corpus import stopwords
from gensim import corpora,models,similarities

abstracts = {}

with open("training_abstracts_1992_2000.json",'r') as f:
	abstracts=json.load(f)

noun_adj_symbol_list = ['NN', 'NNS', 'NNP', 'JJ', 'JJR', 'JJS']
stopwordlist = stopwords.words('english')

remove_non_alphabets = re.compile("[^a-zA-Z\s]")
words_to_update = []


for abstract in abstracts:
	abstract = abstracts[abstract]
	alpha_content = remove_non_alphabets.sub('', abstract['content'].lower())
	content = [word for word in alpha_content.split() if word not in stopwordlist]
	pos_tagged_words = nltk.pos_tag(content)
	words_to_update.append([word for (word, pos_tag) in pos_tagged_words if pos_tag in noun_adj_symbol_list])

dictionary=corpora.Dictionary(words_to_update)

dictionary.compactify()
dictionary.save('abstracts.dict')
id2word = gensim.corpora.Dictionary.load('abstracts.dict')
my_corpus = [dictionary.doc2bow(words) for words in words_to_update] 
corpora.MmCorpus.serialize('abstracts.mm', my_corpus) #CHANGE HERE
