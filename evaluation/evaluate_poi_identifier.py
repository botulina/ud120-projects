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

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 

from sklearn.cross_validation import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.30, random_state=42)
clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
acc = round(accuracy_score(labels_test, pred), 5)
print "Accuracy:", acc
poi = 0
for ii in labels_test:
    if ii == 1:
        poi += 1
print "POIs=", poi
tpos = 0
for n in range(len(pred)):
    if pred[n] == 1 and labels_test[n] == 1:
        tpos += 1
print "True Positive:", tpos
print "Presicion:", precision_score(labels_test, pred)
print "Recall:", recall_score(labels_test, pred)
print f1_score(labels_test, pred)

predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1] 
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

for n in range(len(predictions)):
    if predictions[n] == 0 and true_labels[n] == 0:
        tpos += 1
print "True Positive TEST:", tpos
print "Presicion TEST:", precision_score(true_labels, predictions)
print "Recall TEST:", recall_score(true_labels, predictions)
print f1_score(true_labels, predictions)