import gensim, bz2



id2word = gensim.corpora.Dictionary.load('abstracts.dict')
mm = gensim.corpora.MmCorpus('abstracts.mm')
print id2word
print mm
"""lsi = gensim.models.lsimodel.LsiModel(corpus=mm, id2word=id2word, num_topics=400)
lsi.print_topics(10)"""

print "we are here"