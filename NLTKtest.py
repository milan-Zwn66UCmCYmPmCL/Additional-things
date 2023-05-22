"""
import nltk
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('treebank')
from nltk.tree import *
sent = str(input("say anything: "))
sentence = sent
tokens = nltk.word_tokenize(sentence)
tokens
print(tokens)
tagged = nltk.pos_tag(tokens)
tagged[0:6]
print(tagged)

entities = nltk.chunk.ne_chunk(tagged)
print(entities)

from nltk.corpus import treebank

'''tree = Tree.fromstring(str(entities))
print(tree)
tree.draw()'''

tree = Tree.fromstring(str(entities))
print(tree)
tree.draw()

#t = treebank.parsed_sents('wsj_0001.mrg')[0]
#t.draw()

'''tree = Tree.fromstring(entities)
print(tree)'''
"""