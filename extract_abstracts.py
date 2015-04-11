import re, os, json

base_directory = "/Users/Meghna/Desktop/Spring 2015/Semantic Web Mining/Project/hep-th-abs/"
abstractFile = open("testing_abstracts_2001_2003.json", 'w+')
replace_and = re.compile(' and ')
replace_newline = re.compile('\n')
extract_content = re.compile('\\\\\n\s*(.*)\\\\', re.S)
year = 2001

json_object = {}

for i  in range(3):
	directory = base_directory+str(year+i)
	for file_name in os.listdir(directory):
		file_object = open(directory+"/"+file_name, 'r')
		file_content = file_object.read()
		file_content = file_content.replace('\\\\', '', 1)
		print file_name

		title_group = re.search('Title: (.*)', file_content)
		author_group = re.search('Autho(r|rs): (.*)', file_content)
		content_group = extract_content.search(file_content)

		authors = replace_and.sub(', ', author_group.group(2))
		title = title_group.group(1)
		content = replace_newline.sub(' ', content_group.group(1))

		json_object[file_name.replace('.abs', '')] = { "title": title, "authors": authors, "content": content}

json.dump(json_object, abstractFile)