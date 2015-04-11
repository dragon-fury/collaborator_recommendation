from json import load 
import re, nltk, time
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet, stopwords
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', 
    level=logging.INFO)
from gensim import corpora, models, similarities, matutils
import gensim
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import math

my_corpus = gensim.corpora.MmCorpus('abstracts.mm')
dictionary = gensim.corpora.Dictionary.load('abstracts.dict')
kl=[]

lda = gensim.models.ldamodel.LdaModel(corpus=my_corpus,
        id2word=dictionary,num_topics=122,passes=10)
kl=lda.print_topics()
    


lda.save("abstracts")

with open('topics.txt','w') as f:
    for line in kl:
        f.write(line)
        f.write('\n')

f.close()
