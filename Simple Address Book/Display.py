import xml.etree.ElementTree as ET

# Load XML data
xml_data = '''<?xml version="1.0" encoding="UTF-8"?>
<addressBook>
    <contact>
        <name>John Doe</name>
        <phone>+1234567890</phone>
        <email>johndoe@example.com</email>
    </contact>
    <contact>
        <name>Jane Smith</name>
        <phone>+0987654321</phone>
        <email>janesmith@example.com</email>
    </contact>
    <contact>
        <name>Emily Johnson</name>
        <phone>+1122334455</phone>
        <email>emily.johnson@example.com</email>
    </contact>
</addressBook>'''

# Parse the XML
root = ET.fromstring(xml_data)

# Loop through each contact and print the details
for contact in root.findall('contact'):
    name = contact.find('name').text
    phone = contact.find('phone').text
    email = contact.find('email').text
    print(f"Name: {name}, Phone: {phone}, Email: {email}")
