from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

import nltk
import pandas as pd

df = pd.ExcelFile('test.xlsx').parse('Sheet1') #you could add index_col=0 if there's an index

dataset = df['review_text'].tolist()

# Sample Data


# Creating Tfidf Model
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(dataset)

# Visualizing the Tfidf Model
print(X[0])


# Creating the SVD
lsa = TruncatedSVD(n_components = 4, n_iter = 100)
lsa.fit(X)

row1 = lsa.components_[3]

concept_words = {}

#Visualizing the concepts
terms = vectorizer.get_feature_names()
for i,comp in enumerate(lsa.components_):
    componentTerms = zip(terms,comp)
    sortedTerms = sorted(componentTerms,key=lambda x:x[1],reverse=True)
    sortedTerms = sortedTerms[:100]
    concept_words["Concept " + str(i)] = sortedTerms
    print("\nConcept",i,":")
    for term in sortedTerms:
        print(term)
    
        
#Senetence Cocepr
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