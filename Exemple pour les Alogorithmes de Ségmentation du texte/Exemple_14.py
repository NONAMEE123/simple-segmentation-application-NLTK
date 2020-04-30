'''
Created on 16 juin 2019

@author: KHALID-RAMI
'''
# coding: utf-8
import naftawayh.wordtag as wordtag
import naftawayh
word_list=(u'بالبلاد', u'بينما', u'أو', u'انسحاب', u'انعدام', 
u'انفجار', u'البرنامج', u'بانفعالاتها', u'العربي', u'الصرفي', 
u'التطرف', u'اقتصادي', )
tagger = naftawayh.wordtag.WordTagger();
for word in word_list:
     if tagger.is_noun(word):
         print(u'%s is noun'%word)
     if tagger.is_verb(word):
         print(u'%s is verb'%word)
     if tagger.is_stopword(word):
         print(u'%s is stopword'%word)    