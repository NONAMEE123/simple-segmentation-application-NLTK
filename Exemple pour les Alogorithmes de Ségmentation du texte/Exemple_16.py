# coding: utf-8
import nltk
import googletrans

en_ar = {
    
'CD':'رقم',
'DT':'محدد',
'EX':'وجودي',
'FW':'كلمة اجنبية',
'JJ':'صفة',
'NNS':'اسم الجمع',
'NNP':'اسم علم',
'PRP':'الضمائر الشخصية',
'VB':'فعل',
'VBD':'فعل في الماضي',
'VBP':'فعل في المضارع',
                 
                 }



text_arabe="""uأتشعرُ أنّك مرهقٌ جداً يا فتى؟ متعبٌ من كلّ شيءٍ، وساخطٌ على كلّ شيءْ، تبدُو لِي كذلك، وعيناكَ الضيّقتانِ، تزيدانِ من حدّتكْ، كلّما اكتملتْ تلكَ العقدةُ الّتي تعلُو وجهكْ.
اهدأ، فأنا أستطيعُ أنْ أتفهّم غضبكْ ونقمتكَ على الحياةِ كلّها، وأنتَ تجلسُ كلّ صّباحٍ في هذهِ الزاويةِ المعتمةِ منْ هذا الكوكبِ المقفرِ، تنتظرُ منْ يمرُّ من هُنا راغباً في مسحِ حذائهِ.
"""
tra=googletrans.Translator()
english_text=tra.translate(text_arabe, src="ar", dest="en").text
english_words=nltk.word_tokenize(english_text)
tags=nltk.pos_tag(english_words)

arabic_word= list()
for word, tag in tags:
    if len(word)>1:
        arabic_word.append(tra.translate(text_arabe, src="en", dest="ar").text,en_ar[tag])
    else:
        arabic_word.append(word,en_ar.get(""))
        print(arabic_word)
            

 