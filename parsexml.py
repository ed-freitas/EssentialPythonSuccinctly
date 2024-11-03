import requests
import xml.etree.ElementTree as ET

# Define the URL of the API endpoint
url = "https://www.w3schools.com/xml/note.xml"

# Make the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the XML response
    root = ET.fromstring(response.content)
    print("To:", root.find('to').text)
    print("From:", root.find('from').text)
    print("Heading:", root.find('heading').text)
    print("Body:", root.find('body').text)
else:
    print("Failed to retrieve data:", response.status_code)
