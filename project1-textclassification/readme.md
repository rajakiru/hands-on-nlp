### **Getting Our Dataset**

https://www.cs.cornell.edu/people/pabo/movie-review-data/

### Importing the dataset

```python
reviews = load_files('txt_sentoken/')
X,y = reviews.data,reviews.target
```

X: is for all the different reviews

Y: contains the different classes. Negative: 0 Positive: 1

**Pickling and Unpickling files**

When doing it with large dataset like imdb with 50,00 reviews loading files can take about 15 mins. To make the process faster, once we get x and y we store them as a pickle file in python.

These pickles files are in byte type. W for write, b for byte.

```python
#Pickling the dataset
with open('X.pickle','wb') as f:
    pickle.dump(X,f)
    
with open('y.pickle','wb') as f:
    pickle.dump(y,f)
```

In order to retrieve the files from the pickle file

```python
# Unpickling dataset
X_in = open('X.pickle','rb')
y_in = open('y.pickle','rb')
X = pickle.load(X_in)
y = pickle.load(y_in)
```

### Preprocessing the data

It is done from 0 to 2000, because length of X is 2000 but we can do len(X) as well

```python
# Creating the corpus
corpus = []
for i in range(0, 2000):
    review = re.sub(r'\W', ' ', str(X[i]))
    review = review.lower()
		#removing all the single charecters like i and a
		review = re.sub(r'\s+[a-z]\s+', ' ',review)
    review = re.sub(r'^br$', ' ', review) 
    review = re.sub(r'\s+br\s+',' ',review)
    review = re.sub(r'^b\s+', '', review)
		#removing a lot of spaces with single space
    review = re.sub(r'\s+', ' ', review)
    corpus.append(review)
```

### Creating a bag of words model

We will need a few classes. The max features in 2000

We had to filter the histogram and create the top n words, here max_features sets it too top 2000 words otherwise we’ll have like 15,0000. When we select max_feature  from the histogram **min_dif** will exclude all the words that appears in 3 or less than 3 documents. **Max_df** means that we will exclude all the words that appear in 60% of the document or more like “the” etc. **stopwords** removes the stopwords that we discussed earlier.

```python
# Creating the BOW model
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(max_features = 2000, min_df = 3, max_df = 0.6, stop_words = stopwords.words('english'))
X = vectorizer.fit_transform(corpus).toarray()
```

### Creating a tf-idf model

TF-idf transformer converts the bag of words model into tf-idf model

```python
# Creating the Tf-Idf Model
from sklearn.feature_extraction.text import TfidfTransformer
transformer = TfidfTransformer()
X = transformer.fit_transform(X).toarray()
```

```python
# Creating the Tf-Idf model directly
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(max_features = 2000, min_df = 3, max_df = 0.6, stop_words = stopwords.words('english'))
X = vectorizer.fit_transform(corpus).toarray()
```

### Training and Testing dataset

The train_test_split is a function that splits the data sent for us

So X is our vectorized tf-idf model and y is our classes.

```python
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
text_train, text_test, sent_train, sent_test = train_test_split(X, y, test_size = 0.20, random_state = 0)
```

**Logistic Regression: A quick overview with context to nlp**

The sentiment analysis task is  mainly a binary classification problem to predict whether a given sentence is positive or negative. In our case negative is 0 and positive is 1.

- Each sentence is mapped to a point.
- If the point is greater or equal to than 0.5 than positive else negative.

For example each of these sentences have different points. If point > 0.5 then positive.

> It is going to rain today.
> 

> Today I am not going outside.
> 

> I am going to watch the season premiere.
> 

| Words | going | to | today | i | am | it | is | rain | Points |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sentence 1 | 0 | 0.07 | 0.07 | 0 | 0 | 0.17 | 0.17 | 0.17 | 0.62 |
| Sentence 2 | 0 | 0 | 0.07 | 0.07 | 0.07 | 0 | 0 | 0 | 0.41 |
| Sentence 3 | 0 | 0.05 | 0 | 0.05 | 0.05 | 0 | 0 | 0 | 0.72 |

A **learning algorithm** is a specific type of algorithm whose performance increases with time. Logistic regression is a type of learning algorithm. It learns from a training dataset, the pattern of the data and applies the learned logics on new data for prediction.

![Untitled](https://res.cloudinary.com/practicaldev/image/fetch/s--h7eAC8K7--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://miro.medium.com/max/2872/1%2Ak2bLmeYIG7z7dCyxADedhQ.png)

Here X1, X2, X3 would be the features going, to, today etc. The job of logistic regression is to find the optimal value for the coefficients. So whenever we apply some unknown values, then it can predict the value of y.

For some values of the dependent variable the value of y might be >1 or < 0. But we need to restrict it between 0 and 1. The out will be a sigmoid curve.

![Untitled](https://mengjiesite.files.wordpress.com/2016/06/logistic-curve-svg.png?w=1024)

**Training the classifier**

```python
# Training the classifier
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(text_train,sent_train)
```

### **Testing the Model Performance**

sent_pred is the computer generated result. 

```python
# Testing model performance
sent_pred = classifier.predict(text_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(sent_test, sent_pred)
```

So out of 400, we have an accuracy rate of 339/400 = **84.75%** 

This is with only 2000 rows of max features. If we increase, we should get a higher rating.

**Saving the model as a pickle file**

Now that the classifier is ready we can save it as a pickle file without fitting in our tweets.

When the tweets  come we can’t just do *classifer.predict(”insert tweet”)*, because the classifier expects a vectorized input with 2000 features etc.  We need to vectorize tweet and pass it into the classifier.

```python
# Saving our classifier
with open('classifier.pickle','wb') as f:
    pickle.dump(classifier,f)
    
# Saving the Tf-Idf model
with open('tfidfmodel.pickle','wb') as f:
    pickle.dump(vectorizer,f)
```

**Importing and using the pickle file**

When we creating the test we did fit.transform but now we can do directly to make it fit corpus.
