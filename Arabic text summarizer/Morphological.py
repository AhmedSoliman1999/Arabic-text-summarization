from qalsadi import lemmatizer
import Preprocessing

morpholpgy = []
numberofnouns = []
lemmas=[]
def morphological(Articles):
    lemmer = lemmatizer.Lemmatizer()
    for i in Articles:
        result = []
        x = []
        nouns = []
        for j in i:
            lemmas = lemmer.lemmatize_text(j, return_pos=True)
            result.append(lemmas)
            count = 0
            print(lemmas)
            for l in range(0, len(lemmas)):

                # print(l,lemmas[l])
                if len(lemmas[l]) < 2:
                    continue
                if lemmas[l][1] == "noun":
                    count += 1
                if lemmas[l][1]=="stopword":
                    #print("stop word")
                    j= Preprocessing.RemoveStopingWords2(j,l)

            nouns.append(count)
            #print("b :",j)
            #print("sentance:", lemmas)
           # print("count of nouns:", count)

        numberofnouns.append(nouns)
        morpholpgy.append(result)
    # for i in numberofnouns:
    #     print(i)
    return numberofnouns

