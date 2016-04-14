stopwords = []
with open("stopwords.txt") as f:
	for line in f:
		line = line.strip()
		stopwords.append(line)
mapping_1 = ["databases"]
mapping_2 = ["artificial-intelligence"]
mapping_3 = ["information-retrieval"]
mapping_4 = ["computer-vision"]
tim = ""
with open("data.txt") as f:
	for line in f:
		if "#!" in line:
			print ",".join(tim)
		elif "#f" in line:
			line = line.replace("#f","").replace("_","-").split()
			#line = ([unicode(x,"utf-8") for x in line if x.lower() not in stopwords])
			line = ([x.lower() for x in line if x.lower() not in stopwords])
			if line[0] in mapping_1:
				tim.append("databases")
			elif line[0] in mapping_2:
				tim.append("artificial-intelligence")
			elif line[0] in mapping_3:
				tim.append("information-retrieval")
			elif line[0] in mapping_4:
				tim.append("computer-vision")
			else:
				tim.append("other")
		elif "#*" in line:
			tim = []
		
print tim 
