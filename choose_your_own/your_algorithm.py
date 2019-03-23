#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

from time import time

from sklearn.metrics import accuracy_score

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
# plt.show()
################################################################################

def random_forest_classifier(features_train, labels_train, features_test, labels_test):

	from sklearn.ensemble import RandomForestClassifier
	
	clf = RandomForestClassifier(criterion='entropy', n_estimators=100, min_samples_split=10, warm_start=True)
	
	t0 = time()
	print "Time Started - ", round(t0, 3), "s"
	clf.fit(features_train, labels_train)
	print "RandomForestClassifier(criterion='entropy', n_estimators=100, min_samples_split=10, warm_start=True)", round(time()-t0, 3), "s"

	pred = clf.predict(features_test)
	score = clf.score(features_test, labels_test)

	print "RandomForestClassifier Score", score

	return clf, pred, score


def adaboost(features_train, labels_train, features_test, labels_test):
	from sklearn.ensemble import AdaBoostClassifier
	from sklearn.tree import DecisionTreeClassifier

	clf = AdaBoostClassifier(
		DecisionTreeClassifier(
            max_depth=1,
            min_samples_leaf=1
        ),
        n_estimators=100,
        algorithm="SAMME.R"
    )
	
	t0 = time()
	print "Time Started - ", round(t0, 3), "s"
	clf.fit(features_train, labels_train)
	print "AdaBoostClassifier", round(time()-t0, 3), "s"

	pred = clf.predict(features_test)
	score = clf.score(features_test, labels_test)
	
	print "AdaBoostClassifier Score", score

	return clf, pred, score


def k_near_neighbor_classifier(feature_train, label_train, feature_test, label_test, n):
    from sklearn.neighbors import KNeighborsClassifier
    clf = KNeighborsClassifier(
        n_neighbors=n,
        algorithm='auto',
    )
    clf.fit(feature_train, label_train)
    pred = clf.predict(feature_test)
    acc = clf.score(feature_test, label_test)
    # print 'Score:', acc
    return clf, pred, acc

clf, pred, score = random_forest_classifier(features_train, labels_train, features_test, labels_test)
# RandomForestClassifier - Accuracy Score 0.924


clf2, pred2, score2 = adaboost(features_train, labels_train, features_test, labels_test)
# AdaBoostClassifier Accuracy Score 0.924

best_param_for_knn = {}
for i in range(1, 15):
	clf3, pred3, score3 = k_near_neighbor_classifier(features_train, labels_train, features_test, labels_test, i)
	best_param_for_knn[i] = score3
best_k = max(best_param_for_knn, key=best_param_for_knn.get)
print "Best parameter for knn - ", best_k 
print "With Accuracy - ", best_param_for_knn[best_k]
# K- Nearest Neighbor Accuracy Score: 0.944



### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary


try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
