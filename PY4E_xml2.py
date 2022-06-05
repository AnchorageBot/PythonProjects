# This script loops through and processes xml nodes

# https://www.py4e.com/html3/13-web

# Allows us to extract data from XML without worrying about the rules of XML syntax
import xml.etree.ElementTree as ET

# data in string representation of the XML format
data = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

# converts the string representation of the XML into a “tree” of XML elements
tree = ET.fromstring(data)
# retrieves a Python list of subtrees that represent the user structures in the XML tree
pList = tree.findall('users/user')
print('User count:', len(pList))

# looks at each of the user nodes,  prints the name and id text elements as well as the x attribute from the user node
for item in pList:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))

# Code: http://www.py4e.com/code3/xml2.py
