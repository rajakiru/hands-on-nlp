# Table of Contents
- [Introduction to Markov Chains](introduction-to-markov-chains)
- [Building the Character N-Gram model](building-the-character-N-Gram-model)
- [Building the Word N-Gram model](building-the-word-N-Gram-model)

## Introduction to Markov Chains

- A is a state.
- E is a state.

Probability of A → E : 50%

Probability of A → A : 50%

Probability of E → A : 50%

Probability of E → E : 50%

![Untitled](https://www.kdnuggets.com/wp-content/uploads/tayo_introduction_markov_chains_3.jpg)

When you move from one of these state to another you create a chain or sequence like: AAEA, This is a markov chain.

**An N-gram is a contiguous sequence of n items from a given sample of text or speech**

Item here refer to states in markov chains can cane be characters, words or sentences

N = 2, bigrams

N = 3, trigrams

### **Character N-Gram Models**

Here characters are the states of Markov Chains

> “the bird is flying on the blue sky”
> 
- N = 2
    
    Bigrams = ‘th’, ‘he, ‘e ‘, ‘ b’, ‘bi’, ‘ir’, ‘rd’, ‘ d’ etc
    
- N = 3
    
    Trigrams = ‘the’, ‘he ‘, ‘e b’, ‘ bi’, ‘bir’, ‘ird’, ‘rd ‘ etc
    

We can't get much information from extracting these bigrams or trigrams. How do we use this to do analysis?

We track the character following the trigrams as follows:

| Trigrams | Next |
| --- | --- |
| the |  |
| he  | b |
| e b | i |
|  bi | r |
| bir | d |
| ird |  |

**Word N-Gram Models**

Here word is the state of the markov chain. So for the example above we’d have the following table.

| Trigrams | Next |
| --- | --- |
| the bird is | flying |
| bird is flying | on |
| is flying on  | the |
|  flying on the | blue |
| on the blue | sky |
| the blue sky |  |

**How do we use the n-grams and what is the purpose?**

When we use a large set of data and not just one sentence, we have many options.

| Trigrams | Next |
| --- | --- |
| the bird is | [flying, sleeping, eating] |
| bird is flying | [on, through, on] |
| is flying on  | [the] |
|  flying on the | [blue, red] |
| on the blue | [sky] |
| the blue sky | [.] |

“the bird is sleeping”

“the bird is flying on the red”

This is used by google, on our phones for autocomplete etc.

## Building the Character N-Gram model

Creating the n-gram model by looping through the sentence. Initialize the ngram list and if gram is not there add it to the list of the followed by given characters.

```python
# Order of the grams
n = 3
# Our N-Grams
ngrams = {}
for i in range(len(text)-n):
    gram = text[i:i+n]
    if gram not in ngrams.keys():
        ngrams[gram] = []
    ngrams[gram].append(text[i+n])
```

Testing the n-gram model by providing it with an example, here we set it as the starting gram and generating a string with a length of 100.

```python
currentGram = text[0:n]
result = currentGram
for i in range(100):
    if currentGram not in ngrams.keys():
        break
    possibilities = ngrams[currentGram]
    nextItem = possibilities[random.randrange(len(possibilities))]
    result += nextItem
    currentGram = result[len(result)-n:len(result)]
  
print(result)
```

## Building the Word N-Gram model

Creating list of words first and then looping through the set of words. If gram is not in the ngram list we add it.

```python
n = 2
ngrams = {}
words = nltk.word_tokenize(text)
for i in range(len(words)-n):
    gram = ' '.join(words[i:i+n])
    if gram not in ngrams.keys():
        ngrams[gram] = []
    ngrams[gram].append(words[i+n])
```

Testing the gram, unlike last time we can’t specing length of characters instead we specify limit of words as 30.

```python
currentGram = ' '.join(words[0:n])
result = currentGram
for i in range(30):
    if currentGram not in ngrams.keys():
        break
    possibilities = ngrams[currentGram]
    nextItem = possibilities[random.randrange(len(possibilities))]
    result += ' '+nextItem
    rWords = nltk.word_tokenize(result)
    currentGram = ' '.join(rWords[len(rWords)-n:len(rWords)])

print(result)
```
