import pandas as pd
import random as rand
from nltk import bigrams
from nltk import word_tokenize
from nltk.sentiment.util import mark_negation
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.base import TransformerMixin

data=pd.read_csv("C:/Users/Linux/PycharmProjects/capstone_2020/datasets/IMDB Dataset.csv",delimiter=',')

sentiment_data=zip(data["review"],data["sentiment"])
rand.shuffle(sentiment_data)

train_X, train_y=zip(*sentiment_data[:25])

test_X, test_y=zip(*sentiment_data[25:50])

unigram_bigram_clf=Pipeline([
    ('vectorizer',CountVectorizer(analyzer="word",
                                  ngram_range=(1,2),
                                  tokenizer=word_tokenize,
                                  preprocessor=lambda text: text.replace("<br />"," "),)),
    ('classifier',LinearSVC())
])

unigram_bigram_clf.fit(train_X, train_y)
print unigram_bigram_clf.score(test_X, test_y)
