'''
Created on 16 juin 2019

@author: KHALID-RAMI
'''
# coding=utf8
from qalsadi.analex import Analex
filename="C:\\Users\\KHALID-RAMI\\Desktop\\jjjj.txt"
try:
    myfile=open(filename)
    text=(myfile.read()).decode('utf8');
    if text == None: 
        text=u"السلام عليكم"
except:  
    text=u"أسلم"
print(" given text")
debug=False
limit=500
analyzer=Analex
analyzer.set_debug(debug);
result = analyzer.check_text(text);
print('----------------python format result-------')
print(result)
for i in range(len(result)):
    for analyzed in result[i]:
        print ("-------------one case for word------")
