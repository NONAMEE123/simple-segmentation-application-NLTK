# coding: utf-8
from tkinter import *
from tkinter import ttk
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize,sent_tokenize


abbreviations = {'ma.': 'mais', 'mr.': 'mister', 'bro.': 'brother', 'bro': 'brother', 'mrs.': 'mistress', 'ms.': 'miss', 'jr.': 'junior', 'sr.': 'senior',
                 'i.e.': 'for example', 'e.g.': 'for example', 'vs.': 'versus'}
terminators = ['.',':','؟','،','؛', '!', '?',',',';',':','...','« »','-','_','(',')','Mais','et','de plus','.',
               'en outre','puis','non seulement','encore','de surcroît','ainsi que','également','ou bien',
               'd’un côté','de l’autre','d’une part','d’autre part','afin que','pour que','de peur que','en vue que','.\n',
               'de façon à ce que','car','en effet','effectivement','parce que','puisque','attendu que','vu que','étant donné que',
               'grâce à','à cause de','en raison de','par suite de','dans la mesure où','sous prétexte que','de même que','ainsi que',
             'autant que','plus que','moins que','non moins que','selon que','suivant que','malgré','quoique','bien que','alors que',
               'quel que soit','même si','ce n’est pas que','certes','bien sûr','évidemment','il est vrai que','toutefois','en conclusion','par conséquent',
               'finalement','enfin','à condition que','en admettant que','probablement','sans doute','apparemment','par suite','d’abord','dès lors que','depuis que',
               'tandis que','en même temps','pendant que','au moment où','tandis que','au contraire','pour sa part','d’un autre côté','en dépit de, malgré','au lieu de',
               'و','إِضـــــافَــــةً إِلـــــى ذَلِـــــك',' َثُـــــــم','لَــــيْــــسَ هَـــذا وَحَــــسَـــب بَــــل','أَيْــــضًـــــا','فَـــــوْقَ ذَلِـــــــك','وَكَـــــذَلِــــــك','أَيْـــضًـــــــــــــا','أَو','وَإِمــــــــا','مِــــن جِـــــهَـــة',' َّخِــــــشْــــيَــــةً أَن','تَـــــطَـــــلُــــعًــــا إِلــــى',' ُبِـــحَـــــيْـــث','فِــــعْــــــلاً',' َّبِـــــــمـــا أَن',
               'نَـــــظَــــــرًا لأَن',' ِبِـــفَــــــضْــــــل','بِـــسَـــــــبَــــب',' َعُــــقْــــــــب','بِــــإِعْـــتِـــــبـــار أَنّ',' ّبِــــحُــــجَّــــة أَن','مِـــــثْـــلَ','مِــــثْـــلَـــمـــا','وَكَـــــذَلِـــك','بِــــقَـــــدْرِ ما','أَكْــــثَــــر مِـــــن','أَقَـــــلْ مِـــــن','لا أَقَـــــل مِــــن','حَـــــسَــــب',' ِتِـــــبْـــــعًـــا ل',' َّوَكَــــــأَن','بَـــيْــــنَـــمـــا',
               ' َمَــــهْـــما كــــان','حَـــتـــــى وَإِن','وَحَـــسَــــب','طَــــبْــــعًـــا','صَـــــحـــيـــحٌ أَن','وَلَـــــكِـــن','بِـــإِخْـــتِـــصـــار','وَهَـــــــكـــــذا','إِذَن','وَبــــالـــتــــالـــي','وَبــــالـــتــــالـــي',' ّعَــــلــى شَـــرْطُ أَن','رُبَّـــمـــا','بِـــلا شَـــــك',' َّيَـــبْــــــدو أَن','إِذَن','لِـــحَـــــدِ أَنْ','لِـــذَلِــــــــك','وَبِــــالــــتــــالــــي',
               ' ّبِـــحَــــيْــــثُ أَن',' ّحَـــتّـــــى أَن','أَوَّلاً وَقَـــبْــلَ كُـــلِ شَـــيء','وَأَخـــــيـــرًا','خِـــــــتــــامًــــــا','أَيْ',' ًوَخَـــــاصَــــة','إِلـــــى غَـــيْـــرِ ذَلِـــــك',' ُمِـــــــثْــــل',' ِكَـــمـــا يُـــشـــيــرُ إِلَـــيْــه','وَهَــــذا يَـــنْـــطَـــبِـــقُ عَــلــى',' ِبِــــسَـــبَـــب','إِذَن','وَإِضَـــافـــةً إِلَـــى ذَلِـــك','وَلَــــــكِــن','وَبِـــالــمُـــقَــابِــل','بَـــيْــــنَـــمـــا','مَـــعَ ذَلِــــك','وَبِـــالـــعَـــكْـــسِ مِـــن ذَلِـــك','مِـــنْ جِــــهَـــة أُخْــــرى',
               'رَغْـــــمَ ذَلِـــك','فِــــيـــمـــا عَـــدا','منذ','كلتا','ذو','أولوا','سبحان','قصارى','كان','قد','كُلِّ','كُلَّمَا','أنْ','كُلَّ','هَذِهِ ','مِنْ هَذَا','أَوْ','أَوْ رُبَّمَا','َنَا','َنْتَ','الَّتِي','هَذَا','بَيْنَمَا'                                                   
               ]
wrappers = ['"', "'", ')', ']', '}']

#fonction qui cherche les titres dans le fichier input.txt
    
def find_titles() :
    symb=[",",".","!","?"]
    kki= open("C:\\Users\\dell\\Desktop\\output.txt","w+",encoding="utf8")
    f = open("C:\\Users\\dell\\Desktop\\input.txt", "r",encoding="utf8")
    titles=[ ]
    for x in f:
        existe=False  
        for koko in symb:
            if koko in x :
                existe=True
                
            
        if not(existe):
            titles.append(x[:len(x)-1])
        else :
            kki.write(x)

    kki.close() 

            
    return titles

#fonction qui cherche les phrase  sur  le fichier input.txt

def find_sentences(paragraph):
    end = True
    sentences = []
    while end > -1:
        end = find_sentence_end(paragraph)
        if end > -1:
            sentences.append(paragraph[end:].strip())
            paragraph = paragraph[:end]
    sentences.append(paragraph)
    sentences.reverse()
    return sentences

def find_sentence_end(paragraph):
    [possible_endings, contraction_locations] = [[], []]
    contractions = abbreviations.keys()
    sentence_terminators = terminators + [terminator + wrapper for wrapper in wrappers for terminator in terminators]
    for sentence_terminator in sentence_terminators:
        t_indices = list(find_all(paragraph, sentence_terminator))
        possible_endings.extend(([] if not len(t_indices) else [[i, len(sentence_terminator)] for i in t_indices]))
    for contraction in contractions:
        c_indices = list(find_all(paragraph, contraction))
        contraction_locations.extend(([] if not len(c_indices) else [i + len(contraction) for i in c_indices]))
    possible_endings = [pe for pe in possible_endings if pe[0] + pe[1] not in contraction_locations]
    if len(paragraph) in [pe[0] + pe[1] for pe in possible_endings]:
        max_end_start = max([pe[0] for pe in possible_endings])
        possible_endings = [pe for pe in possible_endings if pe[0] != max_end_start]
    possible_endings = [pe[0] + pe[1] for pe in possible_endings if sum(pe) > len(paragraph) or (sum(pe) < len(paragraph) and paragraph[sum(pe)] == ' ')]
    end = (-1 if not len(possible_endings) else max(possible_endings))
    return end

#fonction Génerale qui Affiche tous les Résultats


def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)
        
if __name__ == '__main__':
    
    
    sentences=[]
with open("C:\\Users\\dell\\Desktop\\output.txt",encoding="utf8") as f:
    while True:
        c = f.read()
        if not c:
            break
    
        sentences.append(c)
    
    k=str(sentences)
    p=k[2:len(k)-1]

    sentences = find_sentences(p)
    print("le texte en entrée est ",sentences)
    print("les titres sont  : " ,find_titles())

    print("le nombre des phrases est : " ,len(sentences))
    cmpt=0
    
    for s in sentences:
        r=s.strip()
        cmpt+=1
  
        if r[-1] in ['.',':','؟','،','؛', '!', '?',',',';',':','...','« »','-','_','(',')','.','.',"'"]:
            print("la phrase" ,cmpt,":"," " ,r[:len(r)-1])        
        else:
            print("la phrase" ,cmpt,":"," " ,r)        
    
    def nb_paragraphe ():
        
        #k= open("C:\\Users\\khalid\\Desktop\\phrases.txt","w+",encoding="utf8")
        f = open("C:\\Users\\dell\\Desktop\\input.txt",encoding="utf8")
        par=1
        endParag=True
        y=0
       
        for x in f:
            if not x.strip() and y==0:
                continue
            
        
            if not x.strip() :
                if endParag==True :
                    par=par+1
                    
                    endParag=False
            else :
                mot=str(x)
                mot=mot.strip(" ")
            
                y=1
                
            
                endParag=True
        
        k.close() 
        
        print("\n le nombre des paragraphes est : ",par)
        nb_paragraphe ()
def find_paragraphes() :
        #k= open("C:\\Users\\khalid\\Desktop\\phrases.txt","w+",encoding="utf8")
        f = open("C:\\Users\\dell\\Desktop\\input.txt",encoding="utf8")
        par=1
        endParag=True
        y=0
        print("paragraphe1")
        for x in f:
            if not x.strip() and y==0:
                continue
            
        
            if not x.strip() :
                if endParag==True :
                    par=par+1
                    print("paragraphe"+str(par))
                    endParag=False
            else :
                mot=str(x)
                mot=mot.strip(" ")
            
                y=1
                print(mot)
            
                endParag=True
        
find_paragraphes()
