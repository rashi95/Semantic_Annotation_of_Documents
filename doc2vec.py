#!/usr/bin/python
# -*- coding: utf-8 -*-
from gensim.models import doc2vec
'''
class LabeledSentence(object):
    """
    A single labeled sentence = text item.
    Replaces "sentence as a list of words" from Word2Vec.
    """
    def __init__(self, words, labels):
        """
        `words` is a list of tokens (unicode strings), `labels` a
        list of text labels associated with this text.
        """
        self.words = words
        self.labels = labels

    def __str__(self):
        return '%s(%s, %s)' % (self.__class__.__name__, self.words, self.labels)

class LabeledLineSentence(object):
    def __init__(self, filename):
        self.filename = filename
    def __iter__(self):
        for uid, line in enumerate(open(self.filename)):
            yield LabeledSentence(words=line.split(), labels= ['SENT_%s' % uid])

data = LabeledLineSentence("doc2vec_data")
it = iter(data)
'''
sentences=doc2vec.TaggedLineDocument("datafile")
model = doc2vec.Doc2Vec(sentences, size=300, window=10, min_count=5, workers=11,alpha=0.025, min_alpha=0.025, dm=0) # use fixed learning rate
	
model.save("doc2vec.model")

mapping = ["databases","artificial-intelligence","information-retrieval","computer-vision","other"]
model = doc2vec.Doc2Vec.load("doc2vec.model")
tim = []
for i in range(5,711810):
	mini = -2.0
	tim = []
	for j in range(0,5):
		calc = model.docvecs.similarity(i,j)
		#print calc
		tim.append([calc,j])
		tim.sort()
	print str(i) + " : " + mapping[tim[-1][1]] + "," + mapping[tim[-2][1]]

