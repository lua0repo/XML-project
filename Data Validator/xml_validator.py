import sys
from lxml import etree

def validate_xml(xml_file, xsd_file):
    # Load the XSD file
    with open(xsd_file, 'rb') as schema_file:
        schema_root = etree.XML(schema_file.read())
        schema = etree.XMLSchema(schema_root)

    # Load the XML file
    with open(xml_file, 'rb') as xml_file:
        xml_doc = etree.parse(xml_file)

    # Validate the XML against the XSD
    if schema.validate(xml_doc):
        print(f"{xml_file} is valid.")
    else:
        print(f"{xml_file} is invalid.")
        print("Validation errors:")
        for error in schema.error_log:
            print(error)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python xml_validator.py <xml_file> <xsd_file>")
        sys.exit(1)

    xml_file = sys.argv[1]
    xsd_file = sys.argv[2]

    validate_xml(xml_file, xsd_file)
