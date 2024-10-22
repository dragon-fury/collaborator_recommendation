import json, ast
import re
import pprint
import sys
import networkx as nx


with open("/Users/Meghna/Desktop/Spring 2015/Semantic Web Mining/Project/training_abstracts_1992_2000.json") as json_file:
    json_data = json.load(json_file)
# data_string = json.dumps(json_data)
#print 'ENCODED:', data_string
#print 'INDENT:', json.dumps(data_string, sort_keys=True, indent=2)    #json_data["authors"]
#data_string["authors"]

# data_array =re.split("\}", data_string[1:])
# print data_array

author_adjacency_matrix = {}
paper_count=0
set_of_authors=set()
for obj in json_data:
	authors_string = json_data[obj]['authors']
	
	reg=re.compile('\s*\(.*?\)+\s*')
	reg1=re.compile('\s*\(.*')
	remove_university=re.compile('Univ.*',re.I)
	remove_comments=re.compile('Comment.*', re.I)
	remove_department=re.compile('(Depart|Dept).*',re.I)
	remove_anything_following_a_number=re.compile('\d+.*',re.I)

	clean_authors=reg.sub('',authors_string)
	clean_authors=reg1.sub('',clean_authors)
	clean_authors=remove_comments.sub('',clean_authors)
	clean_authors=remove_anything_following_a_number.sub('',clean_authors)

	authors = re.split(",",clean_authors)
	authors = map(lambda author: remove_university.sub('', author), authors)
	authors = map(lambda author: remove_department.sub('', author), authors)
	authors = map(lambda author: author.lstrip(), authors)
	authors = map(lambda author: author.rstrip(),  authors)
	authors = filter(None,authors)
	set_of_authors.update(authors)
	

	i=0
	while (i <len(authors)):
		
		if(authors[i] not in author_adjacency_matrix):
			author_adjacency_matrix[authors[i]] = {}
		j=0
		while(j<len(authors)): 
			if(i!=j):
				if authors[j] not in author_adjacency_matrix[authors[i]]:
					author_adjacency_matrix[authors[i]][authors[j]] = paper_count
				author_adjacency_matrix[authors[i]][authors[j]] += 1
			j+=1
		i+=1 

f=open('author_author','w+')
f1=open('Set_of_authors','w+')

json.dump(author_adjacency_matrix,f,indent=4)
sys.stdout = f1
print ",\n ".join(str(x) for x in set_of_authors)
#print set_of_authors
f1.close()

f2=open('console','w+')
sys.stdout = f2
#print(author_adjacency_matrix['R. L. Wilson'])
G=nx.Graph()
f = open('Set_of_authors','r')

for line in f:
	m=re.split(",",line)
	#print(m[0])
	m = map(lambda m: m.strip(), m)
	G.add_node(m[0])
    #print(line)
f.close()
#print(G.nodes())
print(G.number_of_nodes())
#print(G.nodes())
for n in G.nodes():
	#print(n)
	#print(m[0])
	#print(author_adjacency_matrix[m[0]])
	
	for value in author_adjacency_matrix[n]:
		#print(m[0])
		G.add_edge(n,value)
		#print(G.has_edge(n,value))
		#print(G.number_of_edges())
#print(author_adjacency_matrix[u'R. L. Wilson'])
print(G.number_of_edges())
print(G.number_of_nodes())
preds = adamic_adar_index(G)
for u, v, p in preds:
	'(%d, %d) -> %.8f' % (u, v, p)
