stopwords = []
with open("stopwords.txt") as f:
	for line in f:
		line = line.strip()
		stopwords.append(line)
#print stopwords
#tim = []
mapping_1 = ["databases"]
mapping_2 = ["artificial-intelligence"]
mapping_3 = ["information-retrieval"]
mapping_4 = ["computer-vision"]
with open("wiki.txt") as f:
	for line in f:
		line = line.split()
		#line = ([unicode(x,"utf-8") for x in line if x.lower() not in stopwords])
		line = ([x.lower() for x in line if x.lower() not in stopwords])
		print " ".join(line)
