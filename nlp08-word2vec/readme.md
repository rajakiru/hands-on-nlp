# Table of Contents

We learn about models like bag of words, tf-idf model, n-gram model etc. Word2Vec is one such model that is in trend right now and has a lot of research going on.

- [Introduction](#bow-tf-idf-problems)
- [Building the Model](#building-the-model)
- [Word2Vec Model](#word-2-vec-model)

### BOW, TF-IDF problems

- Semantic information of the words is not stored. Even in TF-IDF model we only give more importance to the uncommon word.
- There’s a chance of overfitting the model. Overfitting a scenario when model performs very well with your dataset but fails miserably when applied to any new dataset

When working with them we only care about whether the word appears, we do not think of the probability of it with other words etc.

### **Word2Vec - The solution**

- In this model, each word is represented as a vector of 32 or more dimension instead of a single number.
- Relation between different words are preserved

When representing words as vectors, we can add or subtract vectors. When creating a word2vec model based on a huge corpus of data we can do something like:

King - Man + Women = Queen

Where we will get a vector very similar to queen.

https://jalammar.github.io/illustrated-word2vec/

**Extracting sentence meanings**

“Sachin Tendulkar is the Roger Federer of Cricket”

Roger Federer - tennis + cricket = Sachin Tendulkar

### Building the model

- Scrape through a huge dataset like the whole Wikipedia corpus
- Create a matrix with all the unique words in the dataset. The matrix represents all the unique words in the dataset.

    Testing

    > It is going to rain today.
    >

    > Today I am not going outside.
    >

    > I am going to watch the season premiere.
    >

    Then we get the top 10 words

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

    The number of time the word is associated with the other

    | Word | going | to | today | i | am | it | is | rain | not | outside |
    | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    | going | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 |
    | to  | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |
    | today | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
    | i  | 2 | 1 | 1 | 2 | 2 | 0 | 0 | 0 | 1 | 1 |
    | am | 2 | 1 | 1 | 2 | 2 | 0 | 0 | 0 | 1 | 1 |
    | it | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 0 |
    | is | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 0 |
    | rain | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 0 |
    | not | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 1 |
    | outside | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 1 |

    Matrix B

    Split the matrix into two thin matrices

  | Word | Dimension 1 | Dimension 2 |
  | --- | --- | --- |
  | going |  |  |
  | to  |  |  |
  | today |  |  |
  | i  |  |  |
  | am |  |  |
  | it |  |  |
  | is |  |  |
  | rain |  |  |
  | not |  |  |
  | outside |  |  |

  | Words | going | to | today | i | am | it | is | rain | not | outside |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | Dimension 1 |  |  |  |  |  |  |  |  |  |  |
  | Dimension 2 |  |  |  |  |  |  |  |  |  |  |

  going = (X1going, X2going, …. X300going)


## Word 2 Vec Model

We use gensim to create our word2vec model using gensim model. If you notice the sentence variable will have only 1 sentence

```python
import nltk
import urllib
import bs4 as bs
import re
from gensim.models import Word2Vec

# Gettings the data source
source = urllib.request.urlopen('https://en.wikipedia.org/wiki/Global_warming').read()

# Parsing the data/ creating BeautifulSoup object
soup = bs.BeautifulSoup(source,'lxml')

# Fetching the data
text = ""
for paragraph in soup.find_all('p'):
    text += paragraph.text

# Preprocessing the data
text = re.sub(r'\[[0-9]*\]',' ',text)
text = re.sub(r'\s+',' ',text)
text = text.lower()
text = re.sub(r'\W',' ',text)
text = re.sub(r'\d',' ',text)
text = re.sub(r'\s+',' ',text)

# Preparing the dataset
sentences = nltk.sent_tokenize(text)
sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
```

### Training the Word2Vec Model

It accepts two parameters, the words: list of list and min_count: n ignores all the words that appears less than n time. Here we have it as 1, so it ignores 0 words

```python
# Training the Word2Vec model
model = Word2Vec(sentences, min_count=1)
words = model.wv.vocab
```

### Training the Word2Vec Model

It accepts two parameters, the words: list of list and min_count: n ignores all the words that appears less than n time. Here we have it as 1, so it ignores 0 words

```python
# Training the Word2Vec model
model = Word2Vec(sentences, min_count=1)
words = model.wv.index_to_key

# Finding Word Vectors
vector = model.wv['global']

# Most similar words
similar = model.wv.most_similar('warming')
```

### Pre-trained Word2Vec model

https://code.google.com/archive/p/word2vec/

```python
from gensim.models import KeyedVectors
filename = 'GoogleNews-vectors-negative300.bin'

model = KeyedVectors.load_word2vec_format(filename, binary=True)
model.wv.most_similar('king')
model.wv.most_similar(positive=['king','woman'], negative= ['man'])
```

https://www.analyticsvidhya.com/blog/2019/07/how-to-build-recommendation-system-word2vec-python/
