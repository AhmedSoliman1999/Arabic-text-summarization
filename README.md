# Arabic-text-summarization
Graduation team project to summarize any arabic text using nlp techniques and modified page rank algorithm.

![image](https://user-images.githubusercontent.com/48762703/206574704-613614fc-079c-462c-a5e0-542f3bacd452.png)

![image](https://user-images.githubusercontent.com/48762703/206573196-06f70431-9578-4960-bc92-195d1e999033.png)

# Arabic text summarization 
###   Text summarization is the process of producing a shorter version of a specific text. Automatic summarization techniques have been applied to various domains such as medical, political, news, and legal domains proving that adapting domain-relevant features could improve the summarization performance. Despite the existence of plenty of research work in the domain-based summarization in English and other languages, there is a lack of such work in Arabic due to the shortage of existing knowledge bases.
### The project approach is to summarize Arabic text. Arabic text summarization is one of the natural language processing applications which aims to reduce the original text and return the important information from the original text. Which aims to reduce the time that the reader takes to read the article and provide him with the same important information in the original text.
###Arabic language has a complex morphological structure which makes it difficult to extract nouns, so we use a morphological analyzer that is used to solve the problem of nouns extraction and use nouns extraction to build a graph as initial rank, and cosine similarity was used to weigh the edges between sentences. In summary extraction to prevent redundancy, if the overlapping between the selected sentence and any other sentence in the summary is very high then, this sentence is neglected. A Modified PageRank algorithm was used to extract the summary, this algorithm was used by making the initial rank of the sentence as the number of nouns it has, and the weight of the edge is the cosine similarity between the connected nodes. To evaluate the performance of this approach EASC Corpus is used as a standard.


