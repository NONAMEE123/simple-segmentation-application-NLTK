'''
Created on 14 juin 2019

@author: KHALID-RAMI
'''
# coding: utf-8
import nltk,textblob
text="""it was a long day with my friends"""
wiki=textblob.TextBlob(text)
nltk_tags=nltk.pos_tag(nltk.word_tokenize(text))
textblob_tags = wiki.tags
nltk_words=nltk.word_tokenize(text)
textblob_words = wiki.words
nltk_sentences = nltk.sent_tokenize(text)
textblob_sentences=wiki.sentences


print(f"NlTK Tags =>{nltk_tags}")
print(f"textblob_tags =>{textblob_tags}")
print(f"NlTK Words =>{nltk_words}")
print(f"textblob_word =>{textblob_words}")
print(f"NlTK Sentences =>{nltk_sentences}")
print(f"textblob_senetences =>{textblob_sentences}")





