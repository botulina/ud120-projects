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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print enron_data['ALLEN PHILLIP K'].keys() 
print len(enron_data['ALLEN PHILLIP K'].keys()), "# keys"


poi = 0
for i in enron_data:
    if enron_data[i]["poi"]==1:
        poi += 1
print poi, "POI"

enron_names = open("../final_project/poi_names.txt").read().split('\n')
print len(enron_names), "NAMES"

poi_y = [a for a in enron_names if "(y)" in a]
print len(poi_y), "POI(Y)"

poi_n = [a for a in enron_names if "(n)" in a]
print len(poi_n), "POI(N)"

print enron_data['PRENTICE JAMES']['total_stock_value'], "PRENTICE JAMES']['total_stock_value']"
print enron_data['COLWELL WESLEY']['from_this_person_to_poi'], "['COLWELL WESLEY']['from_this_person_to_poi']"
print enron_data['SKILLING JEFFREY K']['exercised_stock_options'], "['SKILLING JEFFREY K']['exercised_stock_options']"
print enron_data['SKILLING JEFFREY K']['total_payments'], "['SKILLING JEFFREY K']['total_payments']"
print enron_data['FASTOW ANDREW S']['total_payments'], "['FASTOW ANDREW S']['total_payments']"
print enron_data['LAY KENNETH L']['total_payments'], "['LAY KENNETH L']['total_payments']"

email = 0
for i in enron_data:
    if enron_data[i]['email_address'] != 'NaN':
        email += 1
print 'email', email

salary = 0
for i in enron_data:
    if enron_data[i]['salary'] != 'NaN':
        salary += 1
print 'salary', salary

tpymnt = 0
for i in enron_data:
    if enron_data[i]['total_payments'] == 'NaN':
        tpymnt += 1
print tpymnt, "total_payment"
print round(tpymnt / float(len(enron_data)),3) , "total_payments"
poin = 0
poiymnt = 0
for i in enron_data:
    if enron_data[i]['poi'] == True:
        poin +=1
        if enron_data[i]['total_payments'] == 'NaN':
            poiymnt += 1
print poin, "POI #"
print round(poiymnt / float(len(enron_data)),3) , "poi_payments"