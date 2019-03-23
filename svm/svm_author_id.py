#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.metrics import accuracy_score
from sklearn import svm
from collections import Counter


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

# features_train = features_train[:len(features_train)/100] 
# labels_train = labels_train[:len(labels_train)/100] 


#########################################################
### your code goes here ###

classifier = svm.SVC(C=10000.0)

t0 = time()
classifier.fit(features_train, labels_train)
print "training time  SVC, rbf, gamma - scale:", round(time()-t0, 3), "s"

t0 = time()
prediction = classifier.predict(features_test)
print "prediction time SVC, rbf, gamma - scale:", round(time()-t0, 3), "s"

acc_score = accuracy_score(prediction, labels_test)
print "Accuracy Score using SVC, rbf, gamma - scale: ", acc_score

## To obtain prediction of specific test sets
# print "Prediction for 10, 26, and 50", prediction[10], prediction[26], prediction[50]

print Counter(prediction)





#########################################################


