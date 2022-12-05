from flask import Flask
from flask import render_template
import jyserver.Flask as jsf
import os
import string
import Title_EXtraction
import Preprocessing
import ReadData as rd
import Morphological
import Graph
import MPageRank
from self import self
import time
import summary_extraction
import re
import string

New_Articles = []
stemmedlist = []
morpholpgy = []
numberofnouns = []
graphs = []

Articles=[]
New_Articles1=[]
p=[]

def summary(Articles):
    print("------------------")
    print(Articles)
    New_Articles = Preprocessing.apply_preprocessing(Articles)
    print(New_Articles[0])
    stemmedlist = Preprocessing.apply_stemming(New_Articles)
    graphs = Graph.build_graph(self, stemmedlist)
    numberofnouns = Morphological.morphological(New_Articles)
    mpr = MPageRank.modifiedPR(numberofnouns, graphs)
    print(mpr, Articles, graphs)
    Summaryy = summary_extraction.extraction(mpr, Articles, graphs)
    print('----------')
    return Summaryy

def create_title(Articles):
    New_Articles1 = Preprocessing.apply_preprocessing(Articles)
    print("After Preprocessing")
    new_article=' '.join(New_Articles1[0])
    p.append(new_article)
    print(p)
    print(Articles)

    stemmed_article,orig_stem = Preprocessing.apply_stemming2(New_Articles1)
    StemmedText=stemmed_article[0]
    print("After stemming")
    print(StemmedText)
    TF=Title_EXtraction.calculate_termfreq(p)
    print("tf=",TF)
    phrases_frequncies=Title_EXtraction.calculate_PF(StemmedText)
    print("PF=",phrases_frequncies)
    PF_SCORE,phrases_list=Title_EXtraction.get_phrasesList(phrases_frequncies,StemmedText,TF,orig_stem)
    print("phrases list=",phrases_list)
    print("pf_score=",PF_SCORE)
    max_item = max(PF_SCORE)
    index=PF_SCORE.index(max_item)
    print("max score=",max_item)
    print("index=",index)
    stem1=list(phrases_list.keys())[index][0]
    stem2=list(phrases_list.keys())[index][1]
    def get_key(val):
        for key, value in orig_stem.items():
            if val == value:
                return key
    word1=get_key(stem1)
    word2=get_key(stem2)
    title=word1+' '+word2
    print("title=",title)

    return title


app=Flask(__name__,template_folder='templates')
@jsf.use(app)
class App:
    def __init__(self):
        self.input_txt=''

    def take(self):

        x=self.js.document.getElementById('input_txt').value
        #print(type(x))
        Articles = []
        Articles.append(str(x))
        print("--------------")
       # print(Articles)
        out = (summary(Articles))
        print(out[0])
        self.js.document.getElementById('output_txt').value = out[0]


    def create_title(self):
        x = self.js.document.getElementById('input_txt').value
        # print(type(x))
        Articles = []
        Articles.append(str(x))
        print("--------------")
        # print(Articles)
        out = (create_title(Articles))
        print(out)
        self.js.document.getElementById('s_title').value = out


@app.route('/')
def index():
    return App.render(render_template('index.html'))

if __name__ =='__main__':
    app.run(debug=True)


