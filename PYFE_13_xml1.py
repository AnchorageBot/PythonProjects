# This script will parse some XML and extract some data elements from the XML

# https://www.py4e.com/html3/13-web

# Allows us to extract data from XML without worrying about the rules of XML syntax
import xml.etree.ElementTree as ET

# data in string representation of the XML format
data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

# converts the string representation of the XML into a “tree” of XML elements
tree = ET.fromstring(data)
# function searches through the XML tree and retrieves the element that matches the specified tag
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

# Code: http://www.py4e.com/code3/xml1.py
