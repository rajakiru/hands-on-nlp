# Table of Contents

- [Word Synonyms and Antonyms](#word-synonyms-and-antonyms)
- [Word Negation](#word-negation)

## **Word Synonyms and Antonyms**

We will use wordnet: https://wordnet.princeton.edu/

```python
from nltk.corpus import wordnet

# Initializing the list of synnonyms and antonyms
synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for s in syn.lemmas():
        synonyms.append(s.name())
        for a in s.antonyms():
            antonyms.append(a.name())
            
            
# Displaying the synonyms and antonyms
print(set(synonyms))
print(set(antonyms))
```

## **Word Negation**

Negative words like not happy creates a new meaning

```python
import nltk

sentence = "I was not happy with the team's performance"
words = nltk.word_tokenize(sentence)

new_words = []
temp_word = ''
for word in words:
    if word == 'not':
        temp_word = 'not_'
    elif temp_word == 'not_':
        word = temp_word + word
        temp_word = ''
    if word != 'not':
        new_words.append(word)

sentence = ' '.join(new_words)
```

Replace the negative word with antonym
