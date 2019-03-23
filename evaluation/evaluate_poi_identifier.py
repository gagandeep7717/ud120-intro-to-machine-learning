#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
import numpy as np

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)

# Fit data with sklearn decision trees algorithm
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)

# Get the accuracy
from sklearn.metrics import accuracy_score
from sklearn import metrics
prediction = clf.predict(features_test)
print accuracy_score(prediction, labels_test)


# poi_s in labels_test
poi_s_in_label = np.array(labels_test)

print(list(poi_s_in_label).count(1))

# total number of people in test set
print(len(features_test))


# Precision and Recall Metrics

print("Precision - ", float(metrics.precision_score(labels_test, prediction )))
print("Recall - ", metrics.recall_score(labels_test, prediction ))


