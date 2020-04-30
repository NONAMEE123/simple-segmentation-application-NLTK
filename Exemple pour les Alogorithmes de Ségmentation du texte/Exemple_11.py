'''
Created on 15 juin 2019

@author: KHALID-RAMI
'''
# coding=utf8
import pyarabic.arabrepr
from tashaphyne.stemming import ArabicLightStemmer
arepr = pyarabic.arabrepr.ArabicRepr()
repr = arepr.repr
ArListem = ArabicLightStemmer()
word = u'قال'
stem = ArListem.light_stem(word)
print(ArListem.get_stem())
print (ArListem.get_root())
print (ArListem.get_left())
print (ArListem.get_prefix(2))
print (ArListem.get_right())
print (ArListem.get_unvocalized())

    