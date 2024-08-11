# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

import xmltodict
import json


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    # Option 1 parse XML data with Path
    tree = ET.ElementTree(file='05Data.xml')
    root = tree.getroot()
    for child in root:
        print(f'{child.tag}: {child.attrib} ')
    # Top-level elements
    print(root.findall("."))
    # All 'neighbor' grand-children of 'country' children of the top-level  # elements
    print(root.findall("./country/neighbor"))
    # Nodes with name='Singapore' that have a 'year' child
    print(root.findall(".//year/..[@name='Singapore']"))
    # 'year' nodes that are children of nodes with name='Singapore'
    print(root.findall(".//*[@name='Singapore']/year"))
    # All 'neighbor' nodes that are the second child of their parent
    print(root.findall(".//neighbor[2]"))

    # Option 2 to convert the data into Json
    xml_file = open("05Data1.xml", "r")
    xml_string = xml_file.read()
    python_dict = xmltodict.parse(xml_string)
    json_string = json.dumps(python_dict)
    print("The JSON string is:")
    print(json_string)
    print('--------------------Method 1')

    # Option 3 to convert the data into Json
    xml_file = open("05Data2.xml", "r")
    xml_string = xml_file.read()
    root = ET.fromstring(xml_string)
    for actor in root.findall('{http://people.example.com}actor'):
        name = actor.find('{http://people.example.com}name')
        print(name.text)
        for char in actor.findall('{http://characters.example.com}character'):
            print(' |-->', char.text)
    print('--------------------Method 2')

    # Option 4
    ns = {'real_person': 'http://people.example.com',
          'role': 'http://characters.example.com'}
    for actor in root.findall('real_person:actor', ns):
        name = actor.find('real_person:name', ns)
        print(name.text)
        for char in actor.findall('role:character', ns):
            print(' |-->', char.text)
