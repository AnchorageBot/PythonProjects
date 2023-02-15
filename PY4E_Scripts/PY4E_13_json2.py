# This script parses JSON and reads through the data

# https://www.py4e.com/html3/13-web

import json

# a JSON encoding that is roughly equivalent to a string representation of the XML format
# JSON maps directly to some combination of dictionaries and lists
data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

# Creates a Python list; each item within that list is a Python dictionary
info = json.loads(data)
print('User count:', len(info))

#Traverses the Python list called "info"
for item in info:
    # Python index operator [] extracts 'name' data
    print('Name', item['name'])
    # Python index operator [] extracts 'id' data
    print('Id', item['id'])
    #  Python index operator [] extracts 'x' data 
    print('Attribute', item['x'])

# Code: http://www.py4e.com/code3/json2.py
