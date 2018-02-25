# coding: utf-8
#!/usr/bin/env python3
# Dictionaries   132     'learn python the hard way'

'''Python calls them “dicts.” Other languages call them “hashes.”

dict associates one thing to another, no matter what it is
'''

# ex39.py
# create a mapping of state to abbreviation
states = {
  'Oregon': 'OR',
  'Florida': 'FL',
  'California': 'CA',
  'New York': 'NY',
  'Michigan': 'MI'
  }
 
# create a basic set of states and some cities in them
cities = {
  'CA': 'San Francisco',
  'MI': 'Detroit',
  'FL': 'Jacksonville'
  }

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
# print out some cities
print ('- ' * 10)# -------------------------
print ("NY State has: ", cities['NY'])
print ("OR State has: ", cities['OR'])
 # print some states
print (  '- ' * 10)
print ("Michigan's abbreviation is: ", states['Michigan'])
print ("Florida's abbreviation is: ", states['Florida'])

     


# https://www.youtube.com/watch?v=qmWCT_OgrKQ
# http://www.newthinktank.com/2016/07/learn-program-7/
import re

# Your code goes here
find_members = []
for member in dir(re):
    if "find" in member:
        find_members.append(member)

print(sorted(find_members))

# ---------- DICTIONARIES ----------

# While lists organize data based on sequential indexes
# Dictionaries instead use key / value pairs.

# A key / value pair could be
# fName : "Derek" where fName is the key and "Derek" is
# the value

# Create a Dictionary about me
derekDict = {"fName": "Derek",
             "lName": "Banas",
             "address": "123 Main St"
            }

# Get a value with the key
print("May name :", derekDict["fName"])

# Change a value with the key
derekDict["address"] = "215 North St"

# Dictionaries may not print out in the order created
# since they are unordered
print(derekDict)

# Add a new key value
derekDict['city'] = 'Pittsburgh'

# Check if a key exists
print("Is there a city :", "city" in derekDict)

# Get the list of values
print(derekDict.values())

# Get the list of keys
print(derekDict.keys())

# Get the key and value with items()
for k, v in derekDict.items():

    print("Value of derekDict[%s] is %s" % (k, v))
# Get gets a value associated with a key or the default
print(derekDict.get("mName", "Not Here"))

# Delete a key value
del derekDict["fName"]

# Loop through the dictionary keys
for i in derekDict:
    print(i)

# Delete all entries
derekDict.clear()

# List for holding Dictionaries
employees = []
 