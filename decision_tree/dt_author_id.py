#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

from sklearn import tree
from sklearn.metrics import accuracy_score



### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


## Number of features in data
print "Number of features in data", len(features_train[0])


#########################################################
### your code goes here ###
clf_40 = tree.DecisionTreeClassifier(min_samples_split=40)

t0 = time()
clf_40 = clf_40.fit(features_train, labels_train)
print "training time  DT, min min_samples_split = 40:", round(time()-t0, 3), "s"

t0 = time()
pred = clf_40.predict(features_test)
print "Prediction time  DT, min min_samples_split = 40:", round(time()-t0, 3), "s"

acc = accuracy_score(pred, labels_test)
print "Accuracy Score  DT, min min_samples_split = 40:", acc



#########################################################


