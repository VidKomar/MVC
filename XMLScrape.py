"""Testing different scrapers here."""
import requests
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication
print("A laufa?")
# Send a GET request to the XML file URL
url = 'http://agromet.mkgp.gov.si/APP2/AgrometContent/xml/11.xml'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the XML content
    root = ET.fromstring(response.content)

    # Extract temperature data from the XML
    temperatures = []
    for element in root.iter('ty'):
        temperatures.append(float(element.text))

    # Create the graph using matplotlib
    plt.plot(temperatures)
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Variation')
    plt.show()

    # Start the PyQt5 event loop
    app = QApplication([])
    app.exec_()
else:
    print(f'Request failed with status code: {response.status_code}')