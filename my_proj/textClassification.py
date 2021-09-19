
# # Text Classification
#############################################################################
#step1:Loading the dataset i.e. 20Newsgroups 
#############################################################################
from sklearn.datasets import fetch_20newsgroups
twenty_train = fetch_20newsgroups(subset='train', shuffle=True)

#checking the 20 categories in the dataset
twenty_train.target_names
############################################################################
#step2:Extracting features from text files
############################################################################
#2.1building feature vector and removing stop words using CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer
#2.2 Transforming the values in document-matrix into TF-IDF
from sklearn.feature_extraction.text import TfidfTransformer
#building the pipeline for the above process so as to simplify our code 
from sklearn.pipeline import Pipeline
#for nb classifier
from sklearn.naive_bayes import MultinomialNB
text_nb_clf = Pipeline([('vect', CountVectorizer(stop_words='english')), ('tfidf', TfidfTransformer()), 
                     ('clf', MultinomialNB())])
#for svm classifier
from sklearn.linear_model import SGDClassifier
text_svm_clf = Pipeline([('vect', CountVectorizer(stop_words='english')), ('tfidf', TfidfTransformer()),
                         ('clf-svm', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, n_iter=5, random_state=42))])

#######################################################################3##
#step3: training classifiers
#########################################################################

#Naive Bayes classifier
#now fitting our model on the training dataset
text_nb_clf = text_nb_clf.fit(twenty_train.data, twenty_train.target)

#svm classifier
#now fiiting our model on the training dataset 
text_svm_clf = text_svm_clf.fit(twenty_train.data, twenty_train.target)

#########################################################################
#step4 : testing classifiers
########################################################################

#fetching the test data
twenty_test = fetch_20newsgroups(subset='test', shuffle=True)
import numpy as np
#naive bayes
predicted_nb = text_nb_clf.predict(twenty_test.data)
accuracy_nb=np.mean(predicted_nb == twenty_test.target)*100

print("the Naive Bayes model's accuracy is:\t"+str(accuracy_nb))

#support vector machine
predicted_svm = text_svm_clf.predict(twenty_test.data)
accuracy_svm=np.mean(predicted_svm == twenty_test.target)*100

print("the SVM model's accuracy is :\t"+str(accuracy_svm))
