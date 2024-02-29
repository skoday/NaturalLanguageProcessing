import os
import xml.etree.ElementTree as ET
import csv
from datetime import datetime

class Consolidation:
    def __init__(self):
        self.root_folder = "RawData"

    def writingCsv(self, data, csv_file):
        headers = ['Source', 'Title', 'Content', 'Section', 'Url', 'Date']
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            for item in data:
                writer.writerow(item)

    def consolidate(self):
        consolidated_data = []

        for folder_name in os.listdir(self.root_folder):
            folder_path = os.path.join(self.root_folder, folder_name)

            if os.path.isdir(folder_path):
                print(f"Processing: {folder_name}")

                for filename in os.listdir(folder_path):
                    if filename.endswith(".xml"):
                        xml_file_path = os.path.join(folder_path, filename)
                        print(f"Reading: {xml_file_path}")

                        try:
                            tree = ET.parse(xml_file_path)
                            root = tree.getroot()

                            for item in root.findall('item'):
                                title = item.find('title').text
                                content = item.find('description').text
                                pub_date = datetime.strptime(item.find('pubDate').text, '%a, %d %b %Y %H:%M:%S %Z')
                                section = "economia"
                                source = "Jornada"
                                url = item.find('link').text
                                formatted_date = pub_date.strftime('%d/%m/%Y')
                                consolidated_data.append([source, title, content, section, url, formatted_date])

                        except ET.ParseError as e:
                            print(f"Error parsing XML file {xml_file_path}: {e}")
                        except Exception as e:
                            print(f"Error processing XML file {xml_file_path}: {e}")

        if consolidated_data:
            self.writingCsv(consolidated_data, 'consolidated_data.csv')
            print("CSV file generated successfully.")

consolidator = Consolidation()
consolidator.consolidate()





"""import os
import xml.etree.ElementTree as ET
import csv
from datetime import datetime

class Consolidation:

    def __init__(self):
        self.root_folder = "RawData"

    def writingCsv(self, root)

    def consolidate(self):

        for folder_name in os.listdir(self.root_folder):
            folder_path = os.path.join(self.root_folder, folder_name)

            if os.path.isdir(folder_path):
                print(f"Processing: {folder_name}")

                for filename in os.listdir(folder_path):
                    if filename.endswith(".xml"):
                        
                        xml_file_path = os.path.join(folder_path, filename)
                        print(f"Reading: {xml_file_path}")

                        try:
                            tree = ET.parse(xml_file_path)
                            root = tree.getroot()

                            pass
                        except ET.ParseError as e:
                            print(f"Error parsing XML file {xml_file_path}: {e}")
                        except Exception as e:
                            print(f"Error processing XML file {xml_file_path}: {e}")



|root
|consolidation.py
|-RawData
|--2024-02-29
|---archivo.xml
|---archivo.xml
|---archivo.xml
|--2024-03-01
|---archivo.xml
|---archivo.xml

new_object =  Consolidation()
Consolidation.path
"""