'''
Created on 15 juin 2019

@author: KHALID-RAMI
'''

from googletrans import Translator
from nltk.sentiment.util import output_markdown
Translator = Translator()
text = "My name is Rami Khalid and im from Agadir,khadija is my friend."
output = Translator.translate(text, dest="ar", src="en")
print(" Used Language :"+str(Translator.detect(text)))
print(" Translation in arabic :"+output.text)
print(" Source Language :"+output.src)
print(" Destination Language :"+output.dest)
print(output)   