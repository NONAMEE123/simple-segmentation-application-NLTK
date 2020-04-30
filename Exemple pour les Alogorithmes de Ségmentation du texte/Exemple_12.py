'''
Created on 15 juin 2019

@author: KHALID-RAMI
'''
# coding=utf8

import pyarabic.arabrepr
from tashaphyne.stemming import ArabicLightStemmer, ArListem, stem
from pyarabic.arabrepr import arepr
from builtins import repr

arepr=pyarabic.arabrepr.ArabicRepr()
repr=arepr.repr
ArListem = ArabicLightStemmer()
word=u'انلزمكما'
print("light_stem()>>>>>>>")
stem=ArListem.light_stem(word)
print(stem)
print("================================\n")

print("get_stem()>>>>>>>>>")
print(ArListem.get_stem())

print("get_root()>>>>>>>>>")
print(ArListem.get_root())

print("get_root()>>>>>>>>>")
print(ArListem.get_left())

print("get_root()>>>>>>>>>")
print(ArListem.get_prefix())

print("get_root()>>>>>>>>>")
print(ArListem.get_prefix(2))

print("get_root()>>>>>>>>>")
print(ArListem.get_right())

print("get_root()>>>>>>>>>")
print(ArListem.get_suffix())


print("get_root()>>>>>>>>>")
print(ArListem.get_suffix(10))


print("get_root()>>>>>>>>>")
print(ArListem.get_affix())



print("get_root()>>>>>>>>>")
print(ArListem.get_affix_tuple())


print("get_root()>>>>>>>>>")
print(ArListem.get_affix_list())

print("get_root()>>>>>>>>>")
print(ArListem.get_starword())


print("get_root()>>>>>>>>>")
print(ArListem.get_starstem())


print("get_root()>>>>>>>>>")
print(ArListem.get_unvocalized())


