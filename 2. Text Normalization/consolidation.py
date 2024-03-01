import os
import csv
from datetime import datetime
from bs4 import BeautifulSoup
import re

class Consolidation:
    def __init__(self):
        self.root_folder = "RawData"
        self.html_tags = re.compile(r"<.*?>|]]>")
        self.sections = {"economia":"Economía", "tecnologia":"Ciencia y tecnología",
                         "ciencias":"Ciencia y tecnología", "deportes":"Deportes",
                         "cultura":"Cultura"}
        self.sources = {"Jornada":"La Jornada", "Expansion":"Expansión"}

    def writingCsv(self, data, csv_file):
        
        headers = ['Source', 'Title', 'Content', 'Section', 'Url', 'Date']
        file_exists = os.path.exists(
                            os.path.join(self.root_folder, csv_file)
                    )
        
        mode = 'a' if file_exists else 'w'

        with open(csv_file, mode=mode, newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            if not file_exists:
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

                        with open(xml_file_path, "r", encoding="utf-8") as file:
                            data = file.read()

                        soup = BeautifulSoup(data, "xml")
                        items = soup.find_all("item")

                        for item in items:
                            """
                            try:
                                content = item.find("content:encoded").get_text()
                                content = self.html_tags.sub("", content).strip()
                            except:
                                content = item.find("description").get_text()
                            """
                            content = item.find("description").get_text()
                            title = item.find("title").get_text()
                            link = item.find("link").get_text()

                            date = item.find("pubDate").get_text()
                            date_obj = datetime.strptime(date, "%a, %d %b %Y %H:%M:%S %Z")
                            date = date_obj.strftime("%d/%m/%Y")

                            pre_section = xml_file_path.split(" ")[-1].split(".")[0]
                            section = self.sections[pre_section]

                            pre_source = xml_file_path.split("/")[-1].split(" ")[0]
                            source = self.sources[pre_source]

                            consolidated_data.append([source, title, content, section, link, date])

        if consolidated_data:
            self.writingCsv(consolidated_data, 'consolidated_data.csv')
            print("CSV file generated successfully.")
