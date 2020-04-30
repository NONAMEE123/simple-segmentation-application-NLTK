'''
Created on 15 juin 2019

@author: KHALID-RAMI
'''
# coding=utf8
import nltk
from pyarabic import araby

txt = u"هذا النص هو مثال لنص يمكن أن يستبدل في نفس المساحة، لقد تم توليد هذا النص من مولد النص العربى، حيث يمكنك أن تولد مثل هذا النص أو العديد من النصوص الأخرى إضافة إلى زيادة عدد الحروف التى يولدها التطبيق"
wordlist = araby.tokenize(txt)
print(wordlist)
