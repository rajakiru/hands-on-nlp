# Introduction

Table of contents
- [What is NLP?](#what-is-natural-language-processing?) 
- [Python Review](#python-review)
- [Regular Expressions](#what-is-a-regular-expression?)
- [Tokenization](#what-is-tokenization)

## What is Natural Language Processing? 

- Field of study focused on making sense of language
    - using statistics and computers

**NLP application**

- Chatbots
- Translation
- Sentiment analysis

## Python Review

- Variable and Operations
- Conditional Statements
- Loops
- **Lists**
    
    List is a collection which is ordered and changeable. Allows duplicate members.
    
    ```python
    mylist = ["apple", "banana", "cherry"]
    ```
    
- **Tuples**
    
    Tuples is a collection which is ordered and unchangeable. Allows duplicate members.
    
    ```python
    mytuple = ("apple", "banana", "cherry")
    ```
    
- **Dictionaries**
    
    Dictionaries is a collection which is ordered and changeable. No duplicate members.
    
    ```python
    thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
    ```
    
- **List Comprehension**
    
    List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
    
    ```python
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    newlist = []
    
    for x in fruits:
      if "a" in x:
        newlist.append(x)
    ```
    
- Console and File I/O
- Functions
- Classes and Objects

## What is a Regular Expression?

Regular expression or regex is a sequence of characters that defines a specific search pattern and using which you can match or substitute patterns inside a text with least amount of code.

- Strings with a special syntax
- allows us to match patterns in other strings

```python
import re
re.match ('abc','abcdef')
word_regex = '\w+'
re.match(word_regex,'hi there!')
```

| Pattern | Matches | Example |
| --- | --- | --- |
| \w+ | word | ‘Magic’ |
| \d | digit | 9 |
| \s | space | ‘’ |
| .* | wildcard | ‘username74’ |
| + or * | greedy match | ‘aaaaaa’ |
| \S | not space | ‘no_spaces’ |
| [a-z] | lowercase group | ‘abcdefg’ |
- Finding patterns in text
- Substituting patterns in text
- Preprocessing using Regex

## What is tokenization?

- Turning a string or document into **tokens** (smaller chunks)
- One step in preparing a text for NLP
- Many different theories and rules
- Some examples:
    - Breaking out words or sentences
    - Separating punctuation
    - Separating all hashtags in a tweets

**nltk library**

- **nltk**:  natural language toolkit

```python
from nltk.tokenize import word_tokenize
work_tokenize("Hi there!")
```

**Why tokenize?**

- Easier to map part of speech
- Matching common words
- Removing unwanted tokens

**Other nltk tokenizers**

- **sent_tokenize:**  tokenize a document into sentences
- **regexp_tokenize:**  tokenize a string or document based on regular expression pattern
- **TweetTokenizer:** special classes just for tweet tokenization, allowing you to separate hashtags, mentions and a lot of exclamation points!!!
