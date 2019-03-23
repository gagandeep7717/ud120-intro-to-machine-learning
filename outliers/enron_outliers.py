#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
import pandas as pd
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


def find_name_in_dictionary_given_key_value(data, key, value):
	names = data_dict.keys()
	for name in names:
		if data_dict[name][key] == value:
			return name


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
print(data_dict.pop("TOTAL"))


features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

# print(data_dict)

### your code below

for point in data:
	salary = point[0]
	bonus = point[1]
	matplotlib.pyplot.scatter(salary, bonus)




# Find Outliers by bonuses
sorted_array = sorted(data, key = lambda x:x[1])
outliers_by_bonuses = sorted_array[-4:]

names_of_outliers = []
for i in range(len(outliers_by_bonuses)):
	outlier = find_name_in_dictionary_given_key_value(data_dict, 'bonus', outliers_by_bonuses[i][1])
	print outlier
	names_of_outliers.append([outlier, outliers_by_bonuses[i][0], outliers_by_bonuses[i][1]] )

print(names_of_outliers)



matplotlib.pyplot.xlabel("Salary")
matplotlib.pyplot.ylabel("Bonus")
matplotlib.pyplot.show()




