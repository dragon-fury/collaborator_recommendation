import json, ast
import re
import pprint
import sys

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
f1=open('set_of_authors','w+')
json.dump(author_adjacency_matrix,f,indent=4)
sys.stdout = f1
print ",\n ".join(str(x) for x in set_of_authors)
#print set_of_authors