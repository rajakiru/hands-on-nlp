# Table of Contents
- [Latent Semantic Analysis](#latent-semantic-analysis)
- [SVD: Singular Value Decomposition](#svd-singular-value-decomposition)
- [Applications](#applications)

## Latent Semantic Analysis

“**Latent semantic analysis** is a technique of analysing relationships between a set of documents and the terms they contain by producing a set of **concepts** related to the documents and terms”

Example: We have four concepts - 🎵 music, 🍽️ food, 📰 news and 📺 tv.

🎵 Article 1 (85%)

🍽️ Article 3 (100%) , Article 5 (73%)

📰 Article 4 (100%) , Article 6 (100%) , Article 5 (27%)

📺 Article 2 (100%), Article 1 (15%)

How do we separate concepts and generate keywords?

When we use latent semantic analysis we will have a huge value of  data.

| Words | going | to | today | i | am | it | is | rain | not | outside |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sentence 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 0 |
| Sentence 2 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 1 |
| Sentence 3 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |

## SVD: Singular Value Decomposition

![Untitled](https://assets-global.website-files.com/5b1d427ae0c922e912eda447/5feb62f53532cb257a8f901d_open_compressed.jpg)

$$
A[mxn] = U[mxr] * S[rxr] * (V[nxr])^T
$$

**A: Input Data Matrix**

- m x n matrix (m = number of sentences, n = number of words/ features)

**U: Left Singular Matrix**

- m x r matrix (m = number of sentences , r = number of concepts)

**S: Rank Matrix**

- r x r matrix ( r = rank of A)

**V: Right Singular Matrix**

- n x r matrix (n = n = number of words/features, r = number of concepts)

![Untitled](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*iDazFG1YMspV8yz3.jpg)

## Applications

- Article Bucketing in websites
- Finding relations between articles and words
- Page Indexing in search engines

### Building concepts from raw text

Using Latent semantic analysis in python. We use two new libraries TfidfVectorizer and TruncatedSVD.

First we convert all the data into lower case and creating a bag of words model. Tfidfvectorizer automatically creates BOW model and get different features in addition. 

```python
from sklearn.feature_extraction.text import TfidfVectorizer

# Creating Tfidf Model
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(dataset)

# Visualizing the Tfidf Model
print(X[0])
```

Then we need to convert the matrix to the SVD from using the truncated SVD library and then we fit X to create the model. Then we check 1 column.

```python
from sklearn.decomposition import TruncatedSVD
# Creating the SVD
lsa = TruncatedSVD(n_components = 4, n_iter = 100)
lsa.fit(X)

row1 = lsa.components_[3]
```

### Visualizing the concepts

```python
terms = vectorizer.get_feature_names()
for i,comp in enumerate(lsa.components_):
    componentTerms = zip(terms,comp)
    sortedTerms = sorted(componentTerms,key=lambda x:x[1],reverse=True)
    sortedTerms = sortedTerms[:10]
    print("\nConcept",i,":")
    for term in sortedTerms:
        print(term)
```

### Sentence the concepts

```python
for key in concept_words.keys():
    sentence_scores = []
    for sentence in dataset:
        words = nltk.word_tokenize(sentence)
        score = 0
        for word in words:
            for word_with_score in concept_words[key]:
                if word == word_with_score[0]:
                    score += word_with_score[1]
        sentence_scores.append(score)
    print("\n"+key+":")
    for sentence_score in sentence_scores:
        print(sentence_score)
```
