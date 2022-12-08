# Arabic-text-summarization
Graduation team project to summarize any arabic text using nlp techniques and modified page rank algorithm.

![image](https://user-images.githubusercontent.com/48762703/206574704-613614fc-079c-462c-a5e0-542f3bacd452.png)

![image](https://user-images.githubusercontent.com/48762703/206573196-06f70431-9578-4960-bc92-195d1e999033.png)



# Contributors 

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->


<table>
  <tr>
    <td align="center"><a href="https://github.com/AhmedSoliman1999"><img src="![image](https://user-images.githubusercontent.com/48762703/206590489-89dcedb4-d9cc-4e3b-8f41-e86845c45b91.png)
" width="100px;" alt="Ahmed Soliman Image"/><br/><sub><b>Ahmed Soliman</b></sub></a><br/></td>

  </tr>
</table>



# Arabic text summarization 
   Text summarization is the process of producing a shorter version of a specific text. Automatic summarization techniques have been applied to various domains such as medical, political, news, and legal domains proving that adapting domain-relevant features could improve the summarization performance. Despite the existence of plenty of research work in the domain-based summarization in English and other languages, there is a lack of such work in Arabic due to the shortage of existing knowledge bases.
 The project approach is to summarize Arabic text. Arabic text summarization is one of the natural language processing applications which aims to reduce the original text and return the important information from the original text. Which aims to reduce the time that the reader takes to read the article and provide him with the same important information in the original text.
 Arabic language has a complex morphological structure which makes it difficult to extract nouns, so we use a morphological analyzer that is used to solve the problem of nouns extraction and use nouns extraction to build a graph as initial rank, and cosine similarity was used to weigh the edges between sentences. In summary extraction to prevent redundancy, if the overlapping between the selected sentence and any other sentence in the summary is very high then, this sentence is neglected. A Modified PageRank algorithm was used to extract the summary, this algorithm was used by making the initial rank of the sentence as the number of nouns it has, and the weight of the edge is the cosine similarity between the connected nodes. To evaluate the performance of this approach EASC Corpus is used as a standard.


# Introduction

## Motivation
 Due to the massive amount of data written every single day in a different format on the internet since its invention two decades, the desire for automatic text summarization to extract the most important information from the document intensified.
 As people need more time to read the whole text of many documents with the same topic to get the main idea, it is most important to provide an improved mechanism to extract the information quickly and most efficiently. text summarization came to overcome this issue, as it saves time and effort by generating a brief text edition of the source text containing the same ideas without needing to read the whole text. Also, it saves the cost compared with human expert summarization.
 There are many pieces of Research in NLP for Latin languages compared to the Arabic language, especially in the summarization field. Many text summarization researches were conducted for the English language because it is a simple language in its structure and grammar, which is the opposite of the Arabic language, as it has a complex morphological structure which makes it very difficult to extract nouns to be used as a feature for summarization process. Arabic text summarization still suffers from the low performance and the lack of research done in this application of natural language processing.
 There are more than 350 million people who speak Arabic around the world. It is very difficult for those people to manually extract the summary of large documents of text.so, Arabic text summarization is widely required because of the huge number of people that will benefit from an application like this.

## Problem Definition
 Arabic text summarization is one of the challenging open areas for research in natural language processing (NLP) and Researches on forming Arabic text summaries have not been done sufficiently when compared to the research accomplished in English or other languages, this is due to some issues and challenges that slow down the progress in Arabic Natural Language Processing.
 The Arabic language has different problems, represented the Arabic language is a highly derivational and inflectional language, which makes morphological analysis such as lemmatization and stemming a very complex task, the absence of Diacritics that is integral in Arabic texts increases the complexity of inferring s’ meaning, also a language lacks capitalization leading to a great challenge in the process of Named Entity Recognition (NER) system, so it is considered highly ambiguous in comparison to other languages.
 The shape of letters in the Arabic language differs if the letter is in the beginning or the middle or the end of the word, also the Arabic language has three varieties: classical Arabic (found in religious scripts), modern standard Arabic (found in today’s written Arabic and spoken in formal channels), and colloquial or dialectical Arabic (the spoken language), also Arabic dialects vary from one Arab country to another, All these challenges may affect the results of the next process of the text such as summarization, classification, for sentiment analysis these problems and challenges, it led to the difficulties of working in the Arabic language. the poverty of research in it let to the lack of automated Arabic NLP tools such as lexicons, semantic role labelers, and named entity recognition complicate the process more.



## Objective
 Create an application for Arabic text summarization which will:
 • Generate short text.
 • Present the most important content.
 • Extract title for the text.


# Background
 There are three types for text summarization extractive, abstractive and hybrid.
Extractive text summarization: generate a summary by selecting the most important sentences in the text by their score, without changing words in the original text, there are many approaches for extractive vary from simple and complex semantic processing.
Abstractive text summarization: generates a summary like a human’s summary with new sentences by paraphrasing the original text.
Hybrid text summarization: it is a combination between Extractive and Abstractive.

### Extractive text summarization techniques:
 ● Graph-Based approach:
 This method is used to avoid redundancy in the text by using sentence-based graph to describe the text in clusters, by putting sentences similar to each other in the same cluster, then selecting the highest score sentence from each cluster.
 ● Statistical-based approach: It uses statistical analysis to determine the most important words and sentences by word frequency and TF-IDF.
Word frequency: This method score sentence depending on the frequency of each word after removing stop words, this method is the most used for sentence scoring.
TF-IDF: It calculates the word’s importance in the document, and it is better than word frequency in text summarization.
 ● Semantic-based approach:
This method represents the structure of the text using RST, RST is used to know the rhetorical structure between text graphs and build a summary by selecting important text graphs identified by RST.

### Abstractive text summarization techniques:
 ● Sequence to sequence: This is a deep learning method that consists of two parts: encoder and decoder.
 1. First, Input text and reference summary will be tokenized.
 2. Then, they will be encoded by the encoder.
 Encoder: It converts the sequence of words to a sequence of vectors by using convolutional, recurrent, or transformer neural network.
 3. Then, the vector will be passed to the decoder.
 Decoder: it uses the output vector from the encoder to predict the summery sequence on a token per token basis.

### comparison between text summarization algorithms 
![image](https://user-images.githubusercontent.com/48762703/206578424-4de202f4-74dd-435a-899b-babf04e3722b.png)

# Analysis and Design
## System Overview
### System Architecture
![image](https://user-images.githubusercontent.com/48762703/206578994-85d64c03-fc41-4e01-a211-12b48f68ac08.png)

 1. Preprocessing:
     1. We split text into sentences then words
     2. Remove stop words
     3. Apply stemming algorithm
     4. Apply morphological analyzer
 2. Features extraction:
       1. Calculate cosine similarity
       2. Calculate counts of nouns
 3. Build graph: represent the relation between sentences where the vertices represent the sentences Every two vertices are connected with an edge, which has a weight equal to cosine similarity
 4. Apply Modified PageRank: in this step, each sentence is given a special rank that expresses the import of the sentence
 5. Summary Extraction: nodes are sorted depending on their final rank, and add sentences to the summary with check the overlapping between the sentences if then the overlapping is very high then, this sentence is neglected to prevent redundancy.
 6. Evaluate Performance: Calculate accuracy


## System Analysis & Design

### Use Case Diagram

![image](https://user-images.githubusercontent.com/48762703/206580761-d7bba64c-59d3-4067-b55c-94a0106d69ed.png)

### Class Diagram
![image](https://user-images.githubusercontent.com/48762703/206580864-40d6a07e-3c39-46f7-82b9-042c6ea2a19b.png)

### Sequence Diagram 
![image](https://user-images.githubusercontent.com/48762703/206580975-3e376df7-58af-4690-a784-62b30be84b5d.png)



# Dataset:
The dataset used for evaluation is The Essex Arabic Summaries Corpus (EASC) It consists of 153 documents.Each document has five corresponding summaries written by human experts.EASC includes 10 subjects: art, music, environment, politics, sports, health, finance, science, and technology, tourism, religion, and education.



# Implementation and Testing

1. Preprocessing 

This module is concerned with preparing the text. we start by reading the text,then apply Normalization, in this step punctuations, digits and diacritics are eliminated from the sentence, also the letters are restored to their original form in Arabic language.Then,Tokenization which means split text to word and save in list.Then,Take a list of words, remove all stop words in text and finally apply ISRIS Stemmer to extract the root of word to reduce the number of distinct words in the text and find similar words.

![image](https://user-images.githubusercontent.com/48762703/206581248-cd527a82-daaf-46b1-afcd-6055ea4f4274.png)


2. Morphological analysis:
Every word in the sentence takes a tag representing its Part of Speech (POS) position in the sentence like (verb, noun, preposition, etc….) and this help us identify the important words.then we determine count of nouns words in each sentence in text as it will be used as initial rank for modified page rank algorithm.

![image](https://user-images.githubusercontent.com/48762703/206581349-412a806f-a997-4840-a13a-17067c3f874c.png)


3. Building graph:
In this step the text is represented as a graph and the vertices of this graph is sentences and edge between sentences is weighted edge which represents cosine similarity between sentences.
The input of this function is the text after stemming.
We should calculate TF-IDF for the Sentences.

![image](https://user-images.githubusercontent.com/48762703/206581570-f71df911-90f1-4d68-9dca-66fa83774c85.png)


Then calculate cosine similarity between each two sentence and this will be the weighted edge between these two sentences.

![image](https://user-images.githubusercontent.com/48762703/206581704-f2f58d7a-da6a-4eeb-8912-2174229a04bf.png)

![image](https://user-images.githubusercontent.com/48762703/206581741-7caf6deb-cfc3-4dc4-a7c3-110c67b811ac.png)

4. Modified page rank algorithm:
First, give every sentence initial rank equal its own the number of nouns.
Then Apply PageRank algorithm with number of iterations 1000 to update rank of every sentences.
Mpr: New rank for sentence in each iteration.
𝐸(𝑔,𝑣𝑖): edge between sentence and each sentence.
𝑃𝑅(𝑣𝑖):Previous rank of sentence.
N: number of sentences in document.
d: constant number=0.85

![image](https://user-images.githubusercontent.com/48762703/206581855-ad4c89b3-78a2-425f-83c2-d1d72d7d03ea.png)
 5. Summary Extraction:
Sort sentences descending because the sentence that has biggest ranking it is most important and so we are arranged sentences in order of importance.
Then, remove sentences with ranking less than 0.4 and Check cosine similarity between sentences and remove sentence of cosine similarity more than 0.7.

![image](https://user-images.githubusercontent.com/48762703/206581956-7a83c756-6757-42e2-89de-a970eb9b98ae.png)


6. Testing:
The evaluation Matrices that are used to evaluate summary are precision, recall and F-measure. These matrices evaluate summary of the system for the dataset document against five corresponding summaries written by human experts in the dataset.

![image](https://user-images.githubusercontent.com/48762703/206582816-c7e2d55c-e147-4137-90c5-f16deedf0479.png)


7. Evaluation results:
Rouge is essentially a set of metrics for evaluating automatic summarization text.
It works by comparing an automatically produced summary against set of reference summaries(typically human-produced).
Rouge-N: measures unigram,bigram,trigram and higher order n-gram overlap.
Rouge-L: measures longest matching sequence of words.
F-Measure:

![image](https://user-images.githubusercontent.com/48762703/206583257-1fa36cd1-8346-4eac-acac-3abc4f1a9dd1.png)


8. Extract Title
Calculate the phrase score for each key phrase according to the equation:

![image](https://user-images.githubusercontent.com/48762703/206583625-a3a47c03-3295-4b70-8a5d-cdcf98c0c5c4.png)


9.UI Design:
• UI design is implemented using local website.
• Tools used for website:
  * For font end:
      - Html:describe the structre of the web page.Its elements tell the browser how to display the content.
      - CSS: describes how html elements displayed on screen.it controls the layout of the webpage. o JavaScript: is a scripting language that enables us to create             dynamically updating content, control multimedia, animate images, and pretty much everything else.
      - Bootstrap:is the most popular CSS framework.
   * To connect frontend and backend:
      - Flask 


# User Manual

To run local website:
   Installation Guide:
        Install anaconda and python
        From anaconda prompt run these commands:
              pip install jyserver
              pip install qalsadi
              pip install self
              pip install flask

1. Open project file.
![image](https://user-images.githubusercontent.com/48762703/206585908-860bb011-9ff1-4523-9961-f21e223a5b39.png)


2. Replace path of project with cmd and press enter.
![image](https://user-images.githubusercontent.com/48762703/206585996-0ed40307-029e-46cc-b6ed-2bfd79f0785e.png)


3. Write in cmd python main.py and press enter.
![image](https://user-images.githubusercontent.com/48762703/206586145-0dc833a4-0e70-4967-96fb-218f933afe4e.png)


4. Copy address that will appear.
![image](https://user-images.githubusercontent.com/48762703/206586825-f1fd93af-99b6-40f3-aeb5-d57f38ca7282.png)

5. Paste address on browser and insert text you want title for in the input text textbox and click create title button to extract title or summarize to extract summary.
![image](https://user-images.githubusercontent.com/48762703/206586985-7f242fb6-b1bc-4eeb-a069-b188e9615d94.png)


# Conclusion

The Arabic language is spoken by more 300 million people all over the world, and despite that, it suffers from poor researches in it, because it suffers from many problems and challenges.Therefore, The Arabic language is considered one of the strongest and most difficult languages.
Arabic text summarization is of great importance, especially in last period with the massive increase of online documents it become hard to read all of that. Our system saves time for users and make it easier for them, as it displays the important sentences and points in document. One of the most important points of this project is that it supports the Arabic language.
This research tries to enhance the performance of the generated summaries by applying the Modified PageRank algorithm. Morphological analyzer is used to overcome the problems of Arabic structure complexity and to extract nouns to use in the process of building the graph, and cosine similarity was used to weigh the edges between sentences. A Modified PageRank algorithm was used to extract the summary, this algorithm was used by making the initial rank of the sentence as the number of nouns it has, and the weight of the edge is the cosine similarity between the connected nodes.
The process of summarization starts by reading the documents, then normalizing data, removing stop words, stemming, morphological analyzer then finally applying the graph and getting the summary. EASC is used as a standard corpus in the testing stage. According to the results, the Modified PageRank returns better results when the number of iterations used is equal to 1000. Page Rank algorithm returns better results than the methods created before it so we use it and our final F-measure is 60.




