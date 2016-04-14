from __future__ import print_function
import sys, string, random, numpy
from nltk.corpus import reuters
from llda import LLDA
from optparse import OptionParser

parser = OptionParser()
parser.add_option("--alpha", dest="alpha", type="float", help="parameter alpha", default=0.001)
parser.add_option("--beta", dest="beta", type="float", help="parameter beta", default=0.001)
parser.add_option("-k", dest="K", type="int", help="number of topics", default=24)
parser.add_option("-i", dest="iteration", type="int", help="iteration count", default=100)
parser.add_option("-s", dest="seed", type="int", help="random seed", default=None)
parser.add_option("-n", dest="samplesize", type="int", help="dataset sample size", default=6000)
(options, args) = parser.parse_args()
corpus = []
labelset = []
labels = []
stopwords = []
with open("stopwords.txt") as f:
	for line in f:
		line = line.strip()
		stopwords.append(line)
#print stopwords
tim = []
mapping_1 = ["databases"]
mapping_2 = ["artificial-intelligence"]
mapping_3 = ["information-retrieval"]
mapping_4 = ["computer-vision"]
with open("training_data.txt") as f:
	for line in f:
		if "#*" in line:
			tim = []			
			#line = line.replace("#*","").split()
			#line = ([unicode(x,"utf-8") for x in line if x.lower() not in stopwords])
			#line = ([x.lower() for x in line if x.lower() not in stopwords])
			#corpus.append(line)
			
		elif "#!" in line:
			line = line.replace("#!","").split()
			#line = ([unicode(x,"utf-8") for x in line if x.lower() not in stopwords])
			line = ([x.lower() for x in line if x.lower() not in stopwords])
			corpus.append(line)
			labels.append(tim)
		elif "#f" in line:
			line = line.replace("#f","").replace("_","-").split()
			#line = ([unicode(x,"utf-8") for x in line if x.lower() not in stopwords])
			line = ([x.lower() for x in line if x.lower() not in stopwords])
			if line[0] in mapping_1:
				tim.append("Databases")
			elif line[0] in mapping_2:
				tim.append("Artificial-Intelligence")
			elif line[0] in mapping_3:
				tim.append("Information-Retreival")
			elif line[0] in mapping_4:
				tim.append("Computer-Vision")
			else:
				tim.append("Other")
#print (labels)
#labels.append(tim)
labelset = ["Databases","Artificial-Intelligence","Information-Retreival","Computer-Vision","Other"]


llda = LLDA(options.K, options.alpha, options.beta)
llda.set_corpus(labelset, corpus, labels)

print ("M=%d, V=%d, L=%d, K=%d" % (len(corpus), len(llda.vocas), len(labelset), options.K))

for i in range(options.iteration):
    sys.stderr.write("-- %d : %.4f\n" % (i, llda.perplexity()))
    llda.inference()
print ("perplexity : %.4f" % (llda.perplexity()))

phi = llda.phi()
for k, label in enumerate(labelset):
    print ("\n-- label %d : %s" % (k, label))
    for w in numpy.argsort(-phi[k])[:30]:
        print ("%s " % (llda.vocas[w]),end="")
	

