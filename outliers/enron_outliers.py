#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop( "TOTAL", 0 )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)
data = sorted( data, key=lambda data: data[1], reverse=True )
limit = int( len( data ) * 0.1)

### your code below
for point in data[0:]:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

for x in data_dict:
    if (data_dict[x]['salary'] > 1000000 and data_dict[x]['salary'] !='NaN'):
        if data_dict[x]['bonus'] > 5000000:
            print x