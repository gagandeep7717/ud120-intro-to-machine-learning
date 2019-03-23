#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.metrics import accuracy_score


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()



#########################################################
### your code goes here ###
classifier = GaussianNB()

t0 = time()
classifier.fit(features_train, labels_train)
print "training time gNB:", round(time()-t0, 3), "s"

t0 = time()
prediction = classifier.predict(features_test)
print "prediction time gNB:", round(time()-t0, 3), "s"

acc_score = accuracy_score(prediction, labels_test)
print "Accuracy Score using GaussianNB - ", acc_score


clf_multinomial = MultinomialNB()

t1 = time()
clf_multinomial.fit(features_train, labels_train)
print "training time mNB:", round(time()-t1, 3), "s"

t1 = time()
prediction_mNB = clf_multinomial.predict(features_test)
print "prediction time mNB:", round(time()-t1, 3), "s"


acc_score_mNB = accuracy_score(prediction_mNB, labels_test)
print "Accuracy Score using MultinomialNB - ", acc_score_mNB


#########################################################


