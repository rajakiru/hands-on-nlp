# Tokenization

**Table of contents**
- [Introduction](#introduction) 
- [Stemmning and Lemmatization](#stemming-and-lemmatization)
- [POS Tagging](#parts-of-speech-tagging)
- [Named Entity Recognition](#name-entity-of-recognition)

## Introduction

*Tokenization* is a process in which a sequence is broken down into pieces such as words, sentences, phrases etc. In the previous video you have learned how to tokenize a paragraph into sentences or words. The way these tokenizations work are explained as follows.

- ***Word Tokenization:***
    
    In this process a sequence like a sentence or a paragraph is broken down into words. These tokenizations are carried out based on the delimiter "**space**" ("  "). Say, we have a sentence, "the sky is blue". Then here the sentence consist of 4 words with spaces between them. Word tokenization tracks these spaces and returns the list of words in the sentence. `["the","sky","is","blue"]`
    
- ***Sentence Tokenization:***
    
    In this process instead of tokenizing a paragraph based on "**space**", we tokenize it based on "**.**" and "**,**". Therefore, we get all the different sentences consisting the paragraph.
    

We can perform these tokenizations even without the use of **nltk library**. We can use the split() function for this as follows.

```python
str = "I love NLP"
words = str.split(" ")
print(words)
```

`Out: ["I","love","NLP"]`

For sentence tokenization just replace `str.split(" ")`  with `str.split(".")` .

## Stemming and Lemmatization

Stemming is the process of reducing infected or derived words to their word stem, base, or root form.

> John does his work intelligently.
> 

> John is an intelligent man
> 

> John is always working
> 

**Sentence 1**

John 

does 

his 

work

intelligently

**Sentence 2**

John

is

an

intelligent

man

**Sentence 3**

John

is

always 

working

- intelligence, intelligent, intelligently ⇒ intelligen
- going, goes, gone ⇒ go

**Problem**

Produced intermediate representation of the word may not have any meaning.

- Example: intelligen, fina etc.

**Solution: Lemmatization**

Same as Stemming but the intermediate representation/ root form has a meaning.

- intelligence, intelligent, intelligently ⇒ intelligent

**Lemmatization**

- Word representation has meaning.
- Takes more time than stemming.
- Used when meaning of words is important for analysis. Example: question answering application.

**Stemming**

- Word representation may not have meaning.
- Takes less time.
- Used when meaning of words is not as important for analysis. Example: Spam detection.

### **Stemming using NLTK**

```python
stemmer = PorterStemmer()
#Stemming
for i in range(len(sentences)):
	words = nltk.word_tokenize(sentetnces[i])
	newwords = [stemmer.stem(word) for word in words]
	sentences[i] = ''.join(newwords)
```

[stemming.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e83a5aa7-db16-4aba-a9ca-63133213b3e4/stemming.py)

### **Lemmatization using NLTK**

```python
lemmatizer = WordNetLemmatizer()
#Lemmatization
for i in range(len(sentences)):
	words = nltk.word_tokenize(sentetnces[i])
	newwords = [lemmatizer.lemmatize(word) for word in words]
	sentences[i] = ''.join(newwords)
```

[lemmatization.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1c4d6ee5-4e2e-4f31-ab69-3e6a5efd36a3/lemmatization.py)

### **Stop removal using NLTK**

```python
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

sentences = nltk.sent_tokenize(paragraph)

for i in range(len(sentences)):
	words = nltk.word_tokenize(sentetnces[i])
	newwords = [word for word in words if word not in stopwords.words('english')]
	sentences[i] = ''.join(newwords)
```

[stopwords.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/93dd0428-a1d9-41fc-adec-c2c0087b3650/stopwords.py)

## Parts of speech tagging

**POS Tag Meanings**
    
    Here are the meanings of the Parts-Of-Speech tags used in NLTK
    
    | CC | Coordinating conjunction |
    | --- | --- |
    | CD | Cardinal number |
    | DT | Determiner |
    | EX | Existential there |
    | FW | Foreign word |
    | IN | Preposition or subordinating conjunction |
    | JJ | Adjective |
    | JJR | Adjective, comparative |
    | JJS | Adjective, superlative |
    | LS | List item marker |
    | MD | Modal |
    | NN | Noun, singular or mass |
    | NNS | Noun, plural |
    | NNP | Proper noun, singular |
    | NNPS | Proper noun, plural |
    | PDT | Predeterminer |
    | POS | Possessive ending |
    | PRP | Personal pronoun |
    | PRP$ | Possessive pronoun |
    | RB | Adverb |
    | RBR | Adverb, comparative |
    | RBS | Adverb, superlative |
    | RP | Particle |
    | SYM | Symbol |
    | TO | to |
    | UH | Interjection |
    | VB | Verb, base form |
    | VBD | Verb, past tense |
    | VBG | Verb, gerund or present participle |
    | VBN | Verb, past participle |
    | VBP | Verb, non-3rd person singular present |
    | VBZ | Verb, 3rd person singular present |
    | WDT | Wh-determiner |
    | WP | Wh-pronoun |
    | WP$ | Possessive wh-pronoun |
    | WRB | Wh-adverb |

```python
words = nltk.word_tokenize(paragraph)
tagged_word = nltk.pos_tag(words)

word_tags = []
for tw in tagged_words:
	word_tags.append(tw[0]+"_" + tw[1])

tagged_paragraph = ' '.join(word_tags)
```

[postagging.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ae751e52-db87-452b-9247-aec3e087d9e0/postagging.py)

## Name entity of recognition

Every sentences contains a lot of entities. Here is how to extract the different entities in a sentence.

```python
import nltk
paragraph = "The Taj Mahal was built by Emperor Shah Jahan"
                     
# POS Tagging
words = nltk.word_tokenize(paragraph)
tagged_words = nltk.pos_tag(words)

# Named entity recognition
namedEnt = nltk.ne_chunk(tagged_words)
namedEnt.draw()
```

[namedentityrecognition.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5d2b8e60-7f21-4185-abbf-c374557adee5/namedentityrecognition.py)

**Dictionary-based NER**

![image](https://github.com/rajakiru/hands-on-nlp/assets/82876331/7f060d30-d982-4489-a435-b5dc6877c025)


****Rule-based NER****

```python
[_A-Za-z0-9-\+]+(\.[_A-Za-z0-9-]+)*@[A-Za-z0-9-]+(\.[A-Za-z0-9]+)*(\.[A-Za-z]{2,}
```

![image](https://github.com/rajakiru/hands-on-nlp/assets/82876331/289ad820-e450-46dc-b69e-7cacf912841b)

Result will look something like this:
![image](https://github.com/rajakiru/hands-on-nlp/assets/82876331/51d91d52-d2a2-42c5-84ae-d0726a0c9f81)
