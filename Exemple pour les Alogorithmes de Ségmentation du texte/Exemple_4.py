'''
Created on 14 juin 2019

@author: KHALID-RAMI
'''

import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
text = word_tokenize(" hi im khalid and i need to win")
print(nltk.pos_tag(text))

