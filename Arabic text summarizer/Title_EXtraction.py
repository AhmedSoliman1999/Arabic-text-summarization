import math
import Preprocessing
from nltk.util import ngrams

def calculate_termfreq(Articles):
    new_articles=[]
    for i in range(len(Articles)):
        new_articles = Articles[i].split(' ')

    uniquewords = set(new_articles)
    numofwords = dict.fromkeys(uniquewords, 0)
    for word in new_articles:
        numofwords[word] = numofwords[word] + 1

    def computeTF(wordDict, bagofwords):
        tfDict = {}
        bagofwordscount = len(bagofwords)
        for word, count in wordDict.items():
            tfDict[word] = count / float(bagofwordscount)

        return tfDict

    tfa = computeTF(numofwords, new_articles)
    return tfa

def calculate_PF(StemmedText):
    Text=''
    for i in range(0,len(StemmedText)-1):
        Text+=StemmedText[i]

    my_words=Text.split()
    twograms = list(ngrams(my_words, 2))
    print("two grams=",twograms)
    print("twograms len=", len(twograms))

    # print("two grams[0]=",twograms[0])
    #calculate phrase frequency(PF)
    phrases_frequencies={}
    # phrases_frequencies = dict.fromkeys(twograms, None)
    for i in range(0,len(twograms)):
        if(twograms[i] in phrases_frequencies):
            continue
        pf=1
        for j in range(i+1,len(twograms)):
            if(twograms[i]==twograms[j]):
                pf=pf+1

        phrases_frequencies[twograms[i]]=pf
    # for key, value in phrases_frequncies.items():
    #     print(key, value)

    return phrases_frequencies

def get_phrasesList(phrases_frequncies,StemmedText,TF,orig_stem):
    phrases_list = {}
    for key in phrases_frequncies:
        if (phrases_frequncies[key] > 1):
            phrases_list[key] = phrases_frequncies[key]

    print("phrases list 2 =",phrases_list)
    pos1=[]
    pos2=[]
    fr=2

    for i in range(0,len(phrases_list)):
        for j in range(0,len(StemmedText)-1):
            if list(phrases_list.keys())[i][0]+' '+list(phrases_list.keys())[i][1] in StemmedText[j]:
                # print("words=",list(phrases_list.keys())[i][0]+' '+list(phrases_list.keys())[i][1])
                # print("pos=",j)
                phr = StemmedText[j]
                phr1 = phr.split(' ')
                for k in range(0, len(phr1) - 1):

                    if list(phrases_list.keys())[i][0] in phr1[k]:

                        pos1.append(k-2)
                        pos2.append(k-1)
                        break
                break


    if(len(phrases_list)==0):
        print("emptyyyyyyyyyyyyyyyyy")
        fr=1
        pos3=[]
        pos4=[]
        for key in phrases_frequncies:
            if (phrases_frequncies[key] > 0):
                phrases_list[key] = phrases_frequncies[key]

        for i in range(0, len(phrases_list)):
            for j in range(0, len(StemmedText) - 1):
                if list(phrases_list.keys())[i][0] + ' ' + list(phrases_list.keys())[i][1] in StemmedText[j]:
                    # print("words=",list(phrases_list.keys())[i][0]+' '+list(phrases_list.keys())[i][1])

                    # print("pos=",j)
                    phr = StemmedText[j]
                    phr1 = phr.split(' ')

                    # print("phrrrrrrrrr", phr1)
                    for k in range(0, len(phr1) - 1):

                        if list(phrases_list.keys())[i][0] in phr1[k]:
                            pos3.append(k)
                            pos4.append(k + 1)
                            break
                    break

        # print("pos3=",pos3)
        # print("pos3=", pos4)

        # for key, value in phrases_list.items():
    #     print(key, value)
    #calculate ph_pos
    # pos=[]
    # for i in range(0,len(phrases_list)):
    #     for j in range(0,len(StemmedText)-1):
    #         if list(phrases_list.keys())[i][0]+' '+list(phrases_list.keys())[i][1] in StemmedText[j]:
    #             # print("words=",list(phrases_list.keys())[i][0]+' '+list(phrases_list.keys())[i][1])
    #             # print("pos=",j)
    #             pos.append(j)
    #             break

    #calculate PF_score
    def get_key(val):
        for key, value in orig_stem.items():
            if val == value:
                return key

    pf_score=[]
    # print("kkkk=",phrases_frequncies[list(phrases_list.keys())[0]])
    IDF=computeIDF(StemmedText,phrases_list)
    # print("IDF len=",len(IDF))
    for k in range(0,len(phrases_list)):

        word1=get_key(list(phrases_list.keys())[k][0])
        word2=get_key(list(phrases_list.keys())[k][1])
        # if(k==0):
        #     print("word1=",word1)
        #     print("word2=",word2)



        PHF=(phrases_frequncies[list(phrases_list.keys())[0]]/len(StemmedText))

        if(fr==2):
            c = pos1[k] + pos2[k] + 1
            print("pos1=",pos1)
            print("pos2=",pos2)
        else:
            c=pos3[k]+pos4[k]+1




        score=(1/c)+ TF[word1] + TF[word2]+math.log(PHF,2)+(PHF*IDF[k])


        # print("TF1=",TF[list(phrases_list.keys())[k][0]])
        # print("k=",k)
        # print("score",score)
        pf_score.append(score)


    return pf_score,phrases_list

def computeIDF(StemmedText,phrases_list):
    N = len(StemmedText)-1
    IDF=[]

    idfDict = dict.fromkeys(phrases_list.keys(), 0)
    # print("IDF")
    # for key, value in idfDict.items():
    #     print(key, value)
    for word,val in idfDict.items():
        value=phrases_list[word]
        idfDict[word]= math.log(N / float(value))
        IDF.append(idfDict[word])

    return IDF