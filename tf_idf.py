import gensim
from gensim import corpora,models,similarities

dictionary = corpora.Dictionary.load('abstracts.dict') 
corpus = corpora.MmCorpus('abstracts.mm')

tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]

# index = similarities.MatrixSimilarity(tfidf[corpus])
# index.save('tf_idf_abstracts.index')
index = similarities.MatrixSimilarity.load('tf_idf_abstracts.index')
 
new_abstract = "In this talk the class of multifields reductions of the KP and superKP hierarchies leading to nonpurely differential Lax operators is revisited from the point of view of coset construction This means in particular that all the hamiltonian densities of the infinite tower belong to a coset algebra of a given Poisson brackets structure "
vector_new_abstract = dictionary.doc2bow(new_abstract.split())
match_list = index[tfidf[vector_new_abstract]]

docs_by_similarity = sorted(enumerate(match_list), key=lambda item: item[1], reverse=True)
