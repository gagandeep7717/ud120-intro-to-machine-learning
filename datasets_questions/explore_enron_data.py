#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import re


enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

# Find the size of the enron dataset
print "Size of enron data - ", len(enron_data)


# Access first element in the dictionary
all_keys = enron_data.keys()
# print all_keys

# print enron_data.values()[0]

# To find number fo features in, calculate length of dictionary for each person
print "Number of features in enron data - ", len(enron_data.values()[0])

# Calculate number of POIs present in the dataset
number_of_poi = 0

names = enron_data.keys()
list_of_pois = []
for name in names:
	if enron_data[name]['poi'] == 1:
		number_of_poi +=1
		last_first = name.split(' ')[0] + ', ' + name.split(' ')[1]
		list_of_pois.append(last_first)

print "Number of POIs in the enron dataset", number_of_poi

names_in_poi_list = []

with open('../final_project/poi_names.txt') as poi_file:
	for poi in poi_file:
		names_in_poi_list.append(poi[:-1])

names_in_poi_list = names_in_poi_list[2:]

# print names_in_poi_list, "size - ", len(names_in_poi_list)

print "Stock belongings of JAMES PRENTICE - ", enron_data['PRENTICE JAMES']['total_stock_value']

print "Number of emails from WESLEY COLWELL - ", enron_data['COLWELL WESLEY']['from_this_person_to_poi']

print "value of stock options exercised by Jeffrey K Skilling - ", enron_data['SKILLING JEFFREY K']['exercised_stock_options']

board_of_directors = ["SKILLING JEFFREY K", "LAY KENNETH L", "FASTOW ANDREW S"]

for name in board_of_directors:
	print name, enron_data[name]['total_payments']

number_of_people_with_no_salary = 0
number_of_people_with_no_email_address = 0
no_total_payments = 0
poi_with_no_total_payments = 0
for name in all_keys:
	if enron_data[name]['salary'] != 'NaN':
		number_of_people_with_no_salary += 1
	if enron_data[name]['email_address'] != 'NaN':
		number_of_people_with_no_email_address += 1

	if enron_data[name]['total_payments'] == 'NaN':
		no_total_payments += 1

	if enron_data[name]['total_payments'] == 'NaN' and enron_data[name]['poi'] == 1:
		poi_with_no_total_payments += 1

print "number_of_people_with_no_salary - ", number_of_people_with_no_salary
print "number_of_people_with_no_email_address - ", number_of_people_with_no_email_address

print "number of people with no total payment - ", no_total_payments
print len(enron_data)
percentage = float(no_total_payments)/146
print percentage

percentage = float(poi_with_no_total_payments)/146
print percentage





