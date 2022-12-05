from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
graph=[]
vertices_no=0
vertices=[]
# Add a vertex to the set of vertices and the graph
def add_vertex(self,v):
      if v in self.vertices:
        print("Vertex ", v, " already exists")
      else:
        self.vertices_no = self.vertices_no + 1
        self.vertices.append(v)
        if self.vertices_no > 1:
            for vertex in self.graph:
                vertex.append(0)
        temp = []
        for i in range(self.vertices_no):
            temp.append(0)
        self.graph.append(temp)

# Add an edge between vertex v1 and v2 with edge weight e
def add_edge(self,v1, v2, e):
    # Check if vertex v1 is a valid vertex
    if v1 not in self.vertices:
        print("Vertex ", v1, " does not exist.")
    # Check if vertex v1 is a valid vertex
    elif v2 not in self.vertices:
        print("Vertex ", v2, " does not exist.")
    # Since this code is not restricted to a directed or
    # an undirected graph, an edge between v1 v2 does not
    # imply that an edge exists between v2 and v1
    else:
        index1 = self.vertices.index(v1)
        index2 = self.vertices.index(v2)
        self.graph[index1][index2] = e

# Print the graph
def print_graph(self,graph1,vertices_no1,vertex):

  for i in range(vertices_no1):
    for j in range(vertices_no1):
      if graph1[i][j] != 0:
        print(vertex[i], " -> ", vertex[j], \
        " edge weight: ", graph1[i][j])

# Build Graph
def build_graph(self,stemmedlist):
    count = 0
    Graphs = []
    f_vertices_no = []
    vertex = []
    #print(len(stemmedlist))
    for i in range(0, len(stemmedlist)):
        self.vertices = []
        # stores the number of vertices in the graph
        self.vertices_no = 0
        self.graph = []

        for j in range(0, len(stemmedlist[i])-1):
            for k in range(0, len(stemmedlist[i])-1):
                if j == 0:
                    add_vertex(self,k)
                d1 = stemmedlist[i][j]
                d2 = stemmedlist[i][k]

                if d1==' 'or d2==' ':

                    continue

                vector_corpus = [d1, d2]
                vectorizer = TfidfVectorizer()
                tfidf = vectorizer.fit_transform(vector_corpus)
                #print(vectorizer.get_feature_names())
                cs = cosine_similarity(tfidf[0], tfidf[1])
                #print(cs)
                # add_edge(j, k, cs)

                add_edge(self,j, k, cs)

        Graphs.append(self.graph)
        f_vertices_no.append(self.vertices_no)
        vertex.append(self.vertices)
    #print(count)

    # for i in range(0, len(Graphs)):
        # print(print_graph(self,Graphs[i], f_vertices_no[i], vertex[i]))
        # print("------------------------")

    return Graphs


