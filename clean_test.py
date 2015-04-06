import json 
from os import listdir
from os.path import isfile, join
year=1992
list_of_dicts=[]
out={}
outfile=open('out.json','w')

for i in range(0,12):
	
	path="/home/vignesh/code/swm/hep-th-abs/" + str(year+i) + "/"
	onlyfiles = [ f for f in listdir(path) if isfile(join(path,f)) ]

	for files in onlyfiles:
		filepath=path+str(files)
		f=open(filepath,'r')

		i=0

		content=""
		title=""
		authors=""
		for line in f:
			if("Title" in line[0:5]): title=title+line
			if("Authors" in line[0:7]): authors=authors+line
			if(i>1):
				if("\\" in line): continue
				else: content=content+line

			if("\\" in line): i=i+1
			else: continue


		data={}
		id_=files.translate(None,'.abs')
		files=files.replace(".abs",'')
		title=title.replace('Title','')
		authors=authors.replace('Authors','')
		
		data['title']=title.translate(None,'\n')
		data['authors']=authors.translate(None,'\n')
		data['content']=content.translate(None,'\n')
		out[id_]=data

		
		f.close()

json.dump(out,outfile,indent=4)

outfile.close()

