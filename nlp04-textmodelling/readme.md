# Table of Contents 

- [Text Modelling using Bag of Words](#text-modelling-using-bag-of-words)
- [Building the Bag of Words](#building-the-bag-of-words)
- [Text Modelling using TF-IDF model](#text-modelling-using-tf-idf-model)
- [Building the TF-IDF model](#building-the-TF-IDF-model)

## Text Modelling using Bag of Words

Here are some simple sentences and let’s say we want to perform some task using these sentences.

> It is going to rain today.
> 

> Today I am not going outside.
> 

> I am going to watch the season premiere.
> 

We cannot just feed this sentence directly into an algorithm. So let’s create a simple word model using these sentences.

These sentences are already preprocessed (no punctuation). Now we convert to lowercase and then tokenize them.

| Sentence 1 | Sentence 2 | Sentence 3 |
| --- | --- | --- |
| it | today | i |
| is | i | am |
| going | am | going |
| to | not | to |
| rain | going | watch |
| today | outside | the |
|  |  | season |
|  |  | premiere |


**Example Sentences**

| Word | Count |
| --- | --- |
| it | 1 |
| is | 1 |
| going | 3 |
| to  | 2 |
| rain | 1 |
| today | 2 |
| i  | 2 |
| am | 2 |
| not | 1 |
| outside | 1 |
| watch | 1 |
| the | 1 |
| season | 1 |
| premiere | 1 |

**Filtering the matrix**

| Word | Count |
| --- | --- |
| going | 3 |
| to  | 2 |
| today | 2 |
| i  | 2 |
| am | 2 |
| it | 1 |
| is | 1 |
| rain | 1 |
| not | 1 |
| outside | 1 |
| watch | 1 |
| the | 1 |
| season | 1 |
| premiere | 1 |

When we do this with a huge corpus of data we will end up with a huge list of data. So we filter it and here we consider the 10 most frequent words.

| Word | Count |
| --- | --- |
| going | 3 |
| to  | 2 |
| today | 2 |
| i  | 2 |
| am | 2 |
| it | 1 |
| is | 1 |
| rain | 1 |
| not | 1 |
| outside | 1 |

**Creating the matrix**

| Words | going | to | today | i | am | it | is | rain | not | outside |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sentence 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 0 |
| Sentence 2 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 1 |
| Sentence 3 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |

This bag of word model can we fed into any algorithm to analyze the sentences

We will normally have a matrix of 2000 to 4,000 rows. 

## Building the BOW model

- **Preprocessing and Tokenization**: Tokenize the different sentences, Removing the punctuation mark and extra spaces etc
    
    [Bag-Of-Words Model Part 1.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/728169ae-d677-46e2-8783-030dc374b1bd/Bag-Of-Words_Model_Part_1.py)
    
- **Creating histogram of Words and its count**: Loop through the dataset of sentences and tokenize the word, Loop through the words, keep count of the occurences of the word.
    
    [Bag-Of-Words Model Part 2.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2c54d833-e91a-4197-8a97-8cb1f4ffb0b8/Bag-Of-Words_Model_Part_2.py)
    
- **Filtering the words:** Selecting n number of frequencies, using heapq library to find the n most frequent words in the library. Here we 157 words, we can use 100.
    
    [Bag-Of-Words Model Part 3.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/184f1dcd-c6cd-41d5-bb64-09acd3557564/Bag-Of-Words_Model_Part_3.py)
    
- **Bag of words model**: If a word appears  its a 1 and if it does not its a 0. We do this by looping through the sentences, then looping the frequent words and checking it it appears or not.
    
    [Bag-Of-Words Model Part 4.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/949dd8f4-a851-40ac-96c4-f32bb1d8985c/Bag-Of-Words_Model_Part_4.py)
    

## Text Modelling using TF-IDF model

Problems with BOW model

- All words have the same importance
- No semantic information is preserved.
    
    > It is an **amazing** place.
    > 

**TF-IDF Model Intuition**

TF= Term Frequency

IDF= Inverse Document Frequency

TF-IDF = TF * IDF

**Term Frequency** 

$$
Formula = \frac{\text{no. of occurences of a word in a document}}{\text{no. of words in that document}}
$$

Example Sentence: “to be or not to be” 

Tf of “to” is $\frac{1+1}{6}$ = 0.33

This is the term frequency matrix for the example we used previously.

| Word | Sentence 1 | Sentence 2 | Sentence 3 |
| --- | --- | --- | --- |
| going | 0.16 | 0.16 | 0.12 |
| to  | 0.16 | 0 | 0.12 |
| today | 0.16 | 0.16 | 0 |
| i  | 0 | 0.16 | 0.12 |
| am | 0 | 0.16 | 0.12 |
| it | 0.16 | 0 | 0 |
| is | 0.16 | 0 | 0 |
| rain | 0 | 0 | 0 |

**Inverse Document Frequency** 

$$
Formula = log \frac{\text{no. of document}}{\text{no. of documents containing that word}}
$$

Example:

“to be or not to be”

“i have to be”

“you got to be”

Idf of “to” is log $\frac{3}{3}$ = 0

Idf of “be” is log $\frac{3}{3}$ = 0

Idf of “have” is log $\frac{3}{1}$ = 

| Word | idf value |
| --- | --- |
| going | 0 |
| to  | 0.41 |
| today | 0.41 |
| i  | 0.41 |
| am | 0.41 |
| it | 1.09 |
| is | 1.09 |
| rain | 1.09 |

**TF-IDF model**

| Words | going | to | today | i | am | it | is | rain |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sentence 1 | 0 | 0.07 | 0.07 | 0 | 0 | 0.17 | 0.17 | 0.17 |
| Sentence 2 | 0 | 0 | 0.07 | 0.07 | 0.07 | 0 | 0 | 0 |
| Sentence 3 | 0 | 0.05 | 0 | 0.05 | 0.05 | 0 | 0 | 0 |

## Building the TF-IDF model

- Preprocessing, tokenizing and creating the histogram similar to the BOW model.
- **IDF matrix**: Create a dictionary to store each of the words and their idf value. Loop through the frequent words and word in sentence. Use the idf formula.
    
    ```python
    # Creating a IDF Dictionary
    word_idfs = {}
    for word in freq_words:
        doc_count = 0
        for data in dataset:
            if word in nltk.word_tokenize(data):
                doc_count += 1
        word_idfs[word] = np.log(len(dataset)/(1+doc_count))
    ```
    
- **TF matrix:** Contains all the frequent words for each of the sentences and their frequency. So each sentence acts as a vector that stores more value (here 21).
    
    ```python
    # TF Matrix
    tf_matrix = {}
    for word in freq_words:
        doc_tf = []
        for data in dataset:
            frequency = 0
            for w in nltk.word_tokenize(data):
                if word == w:
                    frequency += 1
            tf_word = frequency/len(nltk.word_tokenize(data))
            doc_tf.append(tf_word)
        tf_matrix[word] = doc_tf
    ```
    
- **TF-IDF calculation**: Loop through tf matrix (which contains each of the words mapped with the vectors that contain frequency) and this value is multiplied with idf value.
    
    ```python
    # Creating the Tf-Idf Model
    tfidf_matrix = []
    for word in tf_matrix.keys():
        tfidf = []
        for value in tf_matrix[word]:
            score = value * word_idfs[word]
            tfidf.append(score)
        tfidf_matrix.append(tfidf)
    ```
    
- **TF-IDF matrix:** Right now the tf-idf model is in the form of a list and we need this to be in the form of a matrix.
    
    ```python
    # Finishing the Tf-Tdf model
    X = np.asarray(tfidf_matrix)
    X = np.transpose(X)
    ```
    
    [Tf-Idf Model.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f315cb44-672e-4d65-b836-cc2b6d05e9af/Tf-Idf_Model.py)
