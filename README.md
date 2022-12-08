# Arabic-text-summarization
Graduation team project to summarize any arabic text using nlp techniques and modified page rank algorithm.

![image](https://user-images.githubusercontent.com/48762703/206574704-613614fc-079c-462c-a5e0-542f3bacd452.png)

![image](https://user-images.githubusercontent.com/48762703/206573196-06f70431-9578-4960-bc92-195d1e999033.png)

# Arabic text summarization 
####   Text summarization is the process of producing a shorter version of a specific text. Automatic summarization techniques have been applied to various domains such as medical, political, news, and legal domains proving that adapting domain-relevant features could improve the summarization performance. Despite the existence of plenty of research work in the domain-based summarization in English and other languages, there is a lack of such work in Arabic due to the shortage of existing knowledge bases.
#### The project approach is to summarize Arabic text. Arabic text summarization is one of the natural language processing applications which aims to reduce the original text and return the important information from the original text. Which aims to reduce the time that the reader takes to read the article and provide him with the same important information in the original text.
#### Arabic language has a complex morphological structure which makes it difficult to extract nouns, so we use a morphological analyzer that is used to solve the problem of nouns extraction and use nouns extraction to build a graph as initial rank, and cosine similarity was used to weigh the edges between sentences. In summary extraction to prevent redundancy, if the overlapping between the selected sentence and any other sentence in the summary is very high then, this sentence is neglected. A Modified PageRank algorithm was used to extract the summary, this algorithm was used by making the initial rank of the sentence as the number of nouns it has, and the weight of the edge is the cosine similarity between the connected nodes. To evaluate the performance of this approach EASC Corpus is used as a standard.


# Introduction

## Motivation
#### Due to the massive amount of data written every single day in a different format on the internet since its invention two decades, the desire for automatic text summarization to extract the most important information from the document intensified.
#### As people need more time to read the whole text of many documents with the same topic to get the main idea, it is most important to provide an improved mechanism to extract the information quickly and most efficiently. text summarization came to overcome this issue, as it saves time and effort by generating a brief text edition of the source text containing the same ideas without needing to read the whole text. Also, it saves the cost compared with human expert summarization.
#### There are many pieces of Research in NLP for Latin languages compared to the Arabic language, especially in the summarization field. Many text summarization researches were conducted for the English language because it is a simple language in its structure and grammar, which is the opposite of the Arabic language, as it has a complex morphological structure which makes it very difficult to extract nouns to be used as a feature for summarization process. Arabic text summarization still suffers from the low performance and the lack of research done in this application of natural language processing.
#### There are more than 350 million people who speak Arabic around the world. It is very difficult for those people to manually extract the summary of large documents of text.so, Arabic text summarization is widely required because of the huge number of people that will benefit from an application like this.

## Problem Definition
#### Arabic text summarization is one of the challenging open areas for research in natural language processing (NLP) and Researches on forming Arabic text summaries have not been done sufficiently when compared to the research accomplished in English or other languages, this is due to some issues and challenges that slow down the progress in Arabic Natural Language Processing.
#### The Arabic language has different problems, represented the Arabic language is a highly derivational and inflectional language, which makes morphological analysis such as lemmatization and stemming a very complex task, the absence of Diacritics that is integral in Arabic texts increases the complexity of inferring s’ meaning, also a language lacks capitalization leading to a great challenge in the process of Named Entity Recognition (NER) system, so it is considered highly ambiguous in comparison to other languages.
#### The shape of letters in the Arabic language differs if the letter is in the beginning or the middle or the end of the word, also the Arabic language has three varieties: classical Arabic (found in religious scripts), modern standard Arabic (found in today’s written Arabic and spoken in formal channels), and colloquial or dialectical Arabic (the spoken language), also Arabic dialects vary from one Arab country to another, All these challenges may affect the results of the next process of the text such as summarization, classification, for sentiment analysis these problems and challenges, it led to the difficulties of working in the Arabic language. the poverty of research in it let to the lack of automated Arabic NLP tools such as lexicons, semantic role labelers, and named entity recognition complicate the process more.



## Objective
#### Create an application for Arabic text summarization which will:
#### • Generate short text.
#### • Present the most important content.
#### • Extract title for the text.


# Background
#### There are three types for text summarization extractive, abstractive and hybrid.
#### Extractive text summarization: generate a summary by selecting the most important sentences in the text by their score, without changing words in the original text, there are many approaches for extractive vary from simple and complex semantic processing.
#### Abstractive text summarization: generates a summary like a human’s summary with new sentences by paraphrasing the original text.
#### Hybrid text summarization: it is a combination between Extractive and Abstractive.

### Extractive text summarization techniques:
#### ● Graph-Based approach:
#### This method is used to avoid redundancy in the text by using sentence-based graph to describe the text in clusters, by putting sentences similar to each other in the same cluster, then selecting the highest score sentence from each cluster.
#### ● Statistical-based approach: It uses statistical analysis to determine the most important words and sentences by word frequency and TF-IDF.
Word frequency: This method score sentence depending on the frequency of each word after removing stop words, this method is the most used for sentence scoring.
TF-IDF: It calculates the word’s importance in the document, and it is better than word frequency in text summarization.
#### ● Semantic-based approach:
This method represents the structure of the text using RST, RST is used to know the rhetorical structure between text graphs and build a summary by selecting important text graphs identified by RST.

### Abstractive text summarization techniques:
#### ● Sequence to sequence: This is a deep learning method that consists of two parts: encoder and decoder.
#### 1. First, Input text and reference summary will be tokenized.
#### 2. Then, they will be encoded by the encoder.
#### Encoder: It converts the sequence of words to a sequence of vectors by using convolutional, recurrent, or transformer neural network.
#### 3. Then, the vector will be passed to the decoder.
#### Decoder: it uses the output vector from the encoder to predict the summery sequence on a token per token basis.

### comparison between text summarization algorithms 
![image](https://user-images.githubusercontent.com/48762703/206578424-4de202f4-74dd-435a-899b-babf04e3722b.png)

# Analysis and Design
## System Overview
### System Architecture
![image](https://user-images.githubusercontent.com/48762703/206578994-85d64c03-fc41-4e01-a211-12b48f68ac08.png)

#### 1. Preprocessing:
####      1. We split text into sentences then words
####      2. Remove stop words
####      3. Apply stemming algorithm
####      4. Apply morphological analyzer
#### 2. Features extraction:
####       1. Calculate cosine similarity
####       2. Calculate counts of nouns
#### 3. Build graph: represent the relation between sentences where the vertices represent the sentences Every two vertices are connected with an edge, which has a weight equal to cosine similarity
#### 4. Apply Modified PageRank: in this step, each sentence is given a special rank that expresses the import of the sentence
#### 5. Summary Extraction: nodes are sorted depending on their final rank, and add sentences to the summary with check the overlapping between the sentences if then the overlapping is very high then, this sentence is neglected to prevent redundancy.
  6. Evaluate Performance: Calculate accuracy








