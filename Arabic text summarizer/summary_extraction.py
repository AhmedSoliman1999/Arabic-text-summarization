def extraction(mpr,Articles,graph):
    org_article=[]
    summ=""
    summary=[]
    for article in Articles:
        text=article.split(".")
        org_article.append(text)

    newmpr1 = []
    newmpr=[]
    for i in range (0,len(mpr)):
        #sum_len =length of summary
        sum_len=len(mpr[i])*0.5
        for j in range(0,int(sum_len+1)):
            newmpr1.append(mpr[i][j][0])
        newmpr.append(newmpr1)
        newmpr1=[]
    newmpr=remove_red(graph, newmpr)
    for i in range(0,len(newmpr)):
        newmpr[i]=sorted(newmpr[i])
    # for i in newmpr:
    #     print(i)

    for i in range(0,len(newmpr)):
        for j in range(0,len(newmpr[i])):
          summ+=org_article[i][newmpr[i][j]]+"."
        summary.append(summ)
        summ=""

    #calculate_accurcy(summary)
    return summary

def remove_red(graph,sent_index):
    for k in range(0,len(graph)):
        for i in range(0,len(sent_index[k])):
            x= 1
            j = i + 1
            while x==1:

                if j>=len(sent_index[k]):
                    break
                if j<len(sent_index[k]) and graph[k][sent_index[k][i]][sent_index[k][j]]>0.9:
                    sent_index[k].pop(j)
                    j-=1
                j+=1


    return sent_index

def calculate_accurcy(summary):

    import ReadData
    from rouge import Rouge
    import numpy as np
    from sklearn.metrics import f1_score
    ref = ReadData.read_y()
    r = Rouge()
    ref=np.array(ref)

    avg_Rouge={"rouge1":{"p":0,"r":0,"f":0},"rouge2": {"p": 0, "r": 0, "f": 0},"rougel": {"p": 0, "r": 0, "f": 0}}

    max_Rouge = {"rouge1":{"p":0,"r":0,"f":0},"rouge2": {"p": 0, "r": 0, "f": 0},"rougel": {"p": 0, "r": 0, "f": 0}}



    for i in range(0,len(summary)):
        avg_p1 = 0
        avg_r1 = 0
        avg_f1 = 0
        avg_p2 = 0
        avg_r2 = 0
        avg_f2 = 0
        avg_pl = 0
        avg_rl = 0
        avg_fl = 0
        max_p1 = 0
        max_r1 = 0
        max_f1 = 0
        max_p2 = 0
        max_r2 = 0
        max_f2 = 0
        max_pl = 0
        max_rl = 0
        max_fl = 0
        for k in range(0,5):

            x = r.get_scores(summary[i], ref[i][k])

            avg_p1 += x[0]['rouge-1']['p']
            avg_r1 += x[0]['rouge-1']['r']
            avg_f1 +=x[0]['rouge-1']['f']

            avg_p2 += x[0]['rouge-2']['p']
            avg_r2 += x[0]['rouge-2']['r']
            avg_f2 += x[0]['rouge-2']['f']

            avg_pl += x[0]['rouge-l']['p']
            avg_rl += x[0]['rouge-l']['r']
            avg_fl += x[0]['rouge-l']['f']
            if k==0:
                max_p1 = (x[0]['rouge-1']['p'])
                max_r1 = (x[0]['rouge-1']['r'])
                max_f1 = (x[0]['rouge-1']['f'])
                max_p2 = (x[0]['rouge-2']['p'])
                max_r2 = (x[0]['rouge-2']['r'])
                max_f2 = (x[0]['rouge-2']['f'])
                max_pl = (x[0]['rouge-l']['p'])
                max_rl = (x[0]['rouge-l']['r'])
                max_fl = (x[0]['rouge-l']['f'])
            else:
                if (x[0]['rouge-l']['f'])>max_f1:
                    max_p1 = (x[0]['rouge-1']['p'])
                    max_r1 = (x[0]['rouge-1']['r'])
                    max_f1 = (x[0]['rouge-1']['f'])
                    max_p2 = (x[0]['rouge-2']['p'])
                    max_r2 = (x[0]['rouge-2']['r'])
                    max_f2 = (x[0]['rouge-2']['f'])
                    max_pl = (x[0]['rouge-l']['p'])
                    max_rl = (x[0]['rouge-l']['r'])
                    max_fl = (x[0]['rouge-l']['f'])


        avg_p1 /=5
        avg_r1 /=5
        avg_f1 /=5
        avg_p2 /= 5
        avg_r2 /= 5
        avg_f2 /= 5
        avg_pl /= 5
        avg_rl /= 5
        avg_fl /= 5

        avg_Rouge['rouge1']['p']+=avg_p1
        avg_Rouge['rouge1']['r'] += avg_r1
        avg_Rouge['rouge1']['f'] += avg_f1
        avg_Rouge['rouge2']['p'] += avg_p2
        avg_Rouge['rouge2']['r'] += avg_r2
        avg_Rouge['rouge2']['f'] += avg_f2
        avg_Rouge['rougel']['p'] += avg_pl
        avg_Rouge['rougel']['r'] += avg_rl
        avg_Rouge['rougel']['f'] += avg_fl

        max_Rouge['rouge1']['p'] += max_p1
        max_Rouge['rouge1']['r'] += max_r1
        max_Rouge['rouge1']['f'] += max_f1
        max_Rouge['rouge2']['p'] += max_p2
        max_Rouge['rouge2']['r'] += max_r2
        max_Rouge['rouge2']['f'] += max_f2
        max_Rouge['rougel']['p'] += max_pl
        max_Rouge['rougel']['r'] += max_rl
        max_Rouge['rougel']['f'] += max_fl
    avg_Rouge['rouge1']['p'] /= len(summary)
    avg_Rouge['rouge1']['r'] /= len(summary)
    avg_Rouge['rouge1']['f']/= len(summary)
    avg_Rouge['rouge2']['p'] /= len(summary)
    avg_Rouge['rouge2']['r'] /= len(summary)
    avg_Rouge['rouge2']['f'] /= len(summary)
    avg_Rouge['rougel']['p'] /= len(summary)
    avg_Rouge['rougel']['r'] /= len(summary)
    avg_Rouge['rougel']['f']/= len(summary)

    max_Rouge['rouge1']['p'] /= len(summary)
    max_Rouge['rouge1']['r'] /= len(summary)
    max_Rouge['rouge1']['f'] /= len(summary)
    max_Rouge['rouge2']['p'] /= len(summary)
    max_Rouge['rouge2']['r'] /= len(summary)
    max_Rouge['rouge2']['f'] /= len(summary)
    max_Rouge['rougel']['p'] /= len(summary)
    max_Rouge['rougel']['r'] /= len(summary)
    max_Rouge['rougel']['f'] /= len(summary)
    # print("average = ",avg_Rouge)
    # print("max = ",max_Rouge)
