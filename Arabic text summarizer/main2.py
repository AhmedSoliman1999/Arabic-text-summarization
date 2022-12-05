import os
import string

import Preprocessing
import ReadData as rd
import Morphological
import Graph
import MPageRank
from self import self
import time
import summary_extraction

New_Articles = []
stemmedlist = []
morpholpgy = []
numberofnouns = []
graphs = []
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
lines=[]
while True:
    line=input()
    if line:
        lines.append(line)
    else:
        break
t=' '.join(lines)

print(t)
Articles=[]
Articles.append(t)
print(summary(Articles))