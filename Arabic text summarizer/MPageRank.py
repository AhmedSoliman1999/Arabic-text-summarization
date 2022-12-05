intial_rank=[]
graph=[]
graphs_rank=[]

d=0.85
def modifiedPR(numberofnouns,graphs):
    intial_rank=numberofnouns
    graph_sen_rank = []
    graphs_rank2 = []
    graphs_rank = []
    dic={}
    dic_list=[]
    sorted_list=[]
    # print(len(graphs_rank))
    for i in range(0, len(graphs)):

        dic={}

        count = 0
        for itration in range(0,700):
            graph = graphs[i]


            for indx1 in range(0, len(numberofnouns[i])-1):
                sum = 0

                for indx2 in range(0, len(numberofnouns[i])-1):
                    if (indx1 == indx2):
                        continue
                    if(itration==0):
                        sum += graph[indx1][indx2] * intial_rank[i][indx2]
                    else:

                        sum += graph[indx1][indx2] * graphs_rank[indx2]
                mpr = sum /( len(numberofnouns[i])-2)
                new_rank = (1 - d) + (d * mpr)
                graph_sen_rank.append(new_rank)
                dic[indx1]=new_rank
                #dic_list.append()
            graphs_rank=graph_sen_rank
            graph_sen_rank=[]
            count= count+1

        graphs_rank2.append(dic)


    for i in graphs_rank2:
        sort_orders = sorted(i.items(), key=lambda x: x[1], reverse=True)
        # print(sort_orders)
        sorted_list.append(sort_orders)

    return (sorted_list)