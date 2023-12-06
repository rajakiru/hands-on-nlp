### Text Summarization

Create a summarizer that takes different articles and convert them into mere strings and further summarize all the the articles into 3 or 5 sentences.

**Two methods**

A simple NLP based approach

A deep NLP approach

### Fetching the data

We use beautifulsoup to scrape the data. Type source to print out source. We then parse data to work with string, lxml is a type of parser that is the most efficient. 

We then find all the text in the <p> tag on wikipedia. Some other websites use <div> or <spam> tag.

```python
# Importing the libraries
import bs4 as bs
import urllib.request

# Gettings the data source
source = urllib.request.urlopen('https://en.wikipedia.org/wiki/Global_warming').read()

# Parsing the data/ creating BeautifulSoup object
soup = bs.BeautifulSoup(source,'lxml')
```

### Preprocessing the text

First we remove the references like [1] [32] etc, then we remove the extra spaces. Then we create another variable called clean_text, we clean the text, remove non word characters, all digits, extra spaces with single space.

We use two variables because when we build histogram we use the clean_text, however for summary we use text.

```python
# Preprocessing the data
text = re.sub(r'\[[0-9]*\]',' ',text)
text = re.sub(r'\s+',' ',text)
clean_text = text.lower()
clean_text = re.sub(r'\W',' ',clean_text)
clean_text = re.sub(r'\d',' ',clean_text)
clean_text = re.sub(r'\s+',' ',clean_text)
```

### Tokenization and stop words

In order find the different sentences, we will need to tokenize. We cannot tokenize clean text, because it has no full stops etc.

```python
# Tokenize sentences
sentences = nltk.sent_tokenize(text)

# Stopword list
stop_words = nltk.corpus.stopwords.words('english')
```

### Building the histograms

A histogram with all of the words mapped with the number of times they occur as well as a weighted histogram. 

We don’t won’t the word in stop words and keep track of word count as so.

```python
# Word counts 
word2count = {}
for word in nltk.word_tokenize(clean_text):
    if word not in stop_words:
        if word not in word2count.keys():
            word2count[word] = 1
        else:
            word2count[word] += 1

# Converting counts to weights
for key in word2count.keys():
    word2count[key] = word2count[key]/max(word2count.values())
```

### Sentence Scores

```python
# Product sentence scores    
sent2score = {}
for sentence in sentences:
    for word in nltk.word_tokenize(sentence.lower()):
        if word in word2count.keys():
            if len(sentence.split(' ')) < 25:
                if sentence not in sent2score.keys():
                    sent2score[sentence] = word2count[word]
                else:
                    sent2score[sentence] += word2count[word]
```

### Best 5 sentences

```python
# Word counts 
word2count = {}
for word in nltk.word_tokenize(clean_text):
    if word not in stop_words:
        if word not in word2count.keys():
            word2count[word] = 1
        else:
            word2count[word] += 1

# Converting counts to weights
for key in word2count.keys():
    word2count[key] = word2count[key]/max(word2count.values())
```
