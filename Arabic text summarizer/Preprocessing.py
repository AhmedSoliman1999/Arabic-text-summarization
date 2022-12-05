import re
import string

from Stemming import ShereenKhojaStemmer as shereen_khoja_stemmer
import nltk
#nltk.download('punkt',quiet=True)
from nltk.tokenize import word_tokenize
from nltk.stem.isri import ISRIStemmer
#nltk.download('punkt')
orginal_article=[]
def apply_stemming2(Articles):
    ar_stop_list = open(r"list.txt", encoding="utf-8")
    stop_words = ar_stop_list.read().split('\n')
    st = ISRIStemmer()
   # list1 = []
    stemminglist =[]
    orig_stem={ }
    for i in Articles:
        stems_list = []
        for j in i:
           # print("j=",j)
           text = stemming(j)
           # print("split1=", split1)

           if(j!=' '):
               split1 = j.split(' ')
               split2 = text.split(' ')
               # print("split1=",split1)
               # print("split2=",split2)
               for n in range(1,len(split1)):
                   orig_stem[split1[n]]=split2[n+1]
                   # print("split1_item=", split1[n])
                   # print("split2_item=", split2[n+1])



           # for k in range(0,len(split1)-1):
           #     orig_stem[split1[k]]=split2[k]

           # print("split",split)
           k=0
           # orig_stem = dict.fromkeys(split1, 0)

           stems_list.append(text)
        #list1.append(stems_list)
        stemminglist.append(stems_list)

    #print("*************************")
    # print("orig-stem", orig_stem)


    return stemminglist,orig_stem

def apply_preprocessing(Articles):
    Articles_tokens=[]
    New_Article=[]
    ind1=0
    ind2=0

    for article in Articles:

        N_text = normalizeArabic(article)
        N_text = deNoise(N_text)
        N_text = N_text.split(".")
        orginal_article.append(N_text)
        table = str.maketrans('', '', string.punctuation)
        stripped = [w.translate(table) for w in N_text]
        N_text = RemoveStopingWords(stripped)

        Articles_tokens.append(N_text)
        New_Article.append(N_text)
        ind1+=1
    return New_Article
def stemming(text):
    st = ISRIStemmer()
    s_string = " "
    s=" "
    for i in word_tokenize(text):
        t =st.stem(i)
        s_string = s_string + s + t
    return s_string


def apply_stemming(Articles):
    ar_stop_list = open(r"list.txt", encoding="utf-8")
    stop_words = ar_stop_list.read().split('\n')
    st = ISRIStemmer()
   # list1 = []
    stemminglist =[]
    for i in Articles:
        stems_list = []
        for j in i:
           text = stemming(j)
            #text = shereen_khoja_stemmer.stem(shereen_khoja_stemmer, j)
            #text = RemoveStopingWords2(text)
           # if not text:
            #    text = j
           #0print(text)
           stems_list.append(text)
        #list1.append(stems_list)
        stemminglist.append(stems_list)

    #print("*************************")
    return stemminglist


def normalizeArabic(text):
    text = re.sub("[إأٱآا]", "ا", text)
    text = re.sub("ى", "ي", text)
    text = re.sub("ؤ", "ء", text)
    text = re.sub("ئ", "ء", text)
    text = re.sub("ة", "ه", text)
    text = re.sub("[:“،؟!()»«{}؛]","", text)
    text = re.sub("%", "", text)
    text = re.sub('[٠١٢٣٤٥٦٧٨٩0123456789]', '', text)

    return(text)


def deNoise(text):
    noise = re.compile(""" ّ    | # Tashdid
                             َ    | # Fatha
                             ً    | # Tanwin Fath
                             ُ    | # Damma
                             ٌ    | # Tanwin Damm
                             ِ    | # Kasra
                             ٍ    | # Tanwin Kasr
                             ْ    | # Sukun
                             ـ     # Tatwil/Kashida
                         """, re.VERBOSE)
    text = re.sub(noise, '', text)
    return text

def RemoveStopingWords(text):
    ar_stop_list = open(r"list.txt", encoding="utf-8")
    stop_words = ar_stop_list.read().split('\n')
    needed_words=[]
    s=" "

    for t in text:
        c_string = ""
        tt=t.split()
        for i in tt:
            if i not in (stop_words):
               c_string=c_string+s+i

        needed_words.append(c_string)

    filtered_sentence = " ,".join(needed_words)

    return needed_words
def RemoveStopingWords2(text,word):
    s=" "
    c_string = ""
    #print("before",text)
    #print("index",word)
    tt=text.split()
    for i in range(0,len(tt)):
        if i != word:
           c_string=c_string+s+tt[i]
    #print("after",c_string)
    return c_string
