'''
Created on 14 juin 2019

@author: KHALID-RAMI
'''
# coding: utf-8
import nltk
from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()

word_data = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"
nltk_tokens = nltk.word_tokenize(word_data)
for w in nltk_tokens:
    print(w,"==>",porter_stemmer.stem(w))
