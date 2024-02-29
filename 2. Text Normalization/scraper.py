from bs4 import BeautifulSoup
import requests
import os
from datetime import datetime

class LaJornada:

    url = None
    #sections = None
    sectionsUrl =  None

    def __init__(self):
        self.url = "https://www.jornada.com.mx/v7.0/cgi/rss.php"

    def getSectionsUrl(self, sections = None):
        """"
        Recieves a list wich parameters should be the desired sections.
        If no sections are specified every single section will be downloaded.
        Available sections are shown in the list below.
        """

        if sections == None:
            sections = ['Edición completa', 'Últimas noticias (Noticias de hoy)', 'Opinión', 'Política'
                        ,'Economía', 'Mundo', 'Estados', 'Capital', 'Sociedad y Justicia', 'Ciencias'
                        , 'Cultura', 'Gastronomia', 'Espectáculos', 'Deportes', 'Cartones', 'Videos']
        
        try:
            response = requests.get(self.url)

            if response.status_code == 200:

                urls = []
                
                soup = BeautifulSoup(response.content,'html.parser')

                # Getting items that save contents
                items = soup.find_all('div', class_='item')

                # Distilling relevant urls
                for item in items:
                    span = item.find('span')

                    if span and span.text.strip() in sections:
                        urls.append("https://www.jornada.com.mx" + item.a['href'])

                self.sectionsUrl = urls

            else:
                print(f"Page returned status code: {response.status_code}")
        
        except requests.RequestException as e:
            print(f"Error: {e}")

    def downloadNews(self):
        """
        Download the xml files and save them in a folder wich name is today's date
        that is within RawData
        """
        todayDate = datetime.today().strftime('%Y-%m-%d')

        folderPath = os.path.join("RawData", todayDate)

        if not os.path.exists(folderPath):
            os.makedirs(folderPath)
            print(f"Folder {folderPath} was created")
        else:
            print("A folder with todays data already exists")

        # Downloading FIles
        for url in self.sectionsUrl:
            fileName = url.split('/')[-1].split('?')[0]
            filePath = os.path.join(folderPath, "Jornada - "+fileName)

            response = requests.get(url)

            # Saving file
            with open(filePath, "wb") as file:
                file.write(response.content)

class Expansion:

    url = None
    sectionsUrl = None
    headers = None

    def __init__(self) -> None:
        self.url = "https://expansion.mx/canales-rss"
        self.headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'
                        }

    def getSectionsUrl(self, sections = None):
        """"
        Recieves a list wich parameters should be the desired sections.
        If no sections are specified every single section will be downloaded.
        Available sections are shown in the list below.
        """

        if sections == None:
            sections = ['economia', 'tecnologia']
    
        try:
            response = requests.get(self.url, headers = self.headers)

            if response.status_code == 200:

                urls = []

                # Distilling relevant urls
                for section in sections:
                    urls.append("https://expansion.mx/rss/"+section)

                self.sectionsUrl = urls

            else:
                print(f"Expansion Page returned status code: {response.status_code}")
        
        except requests.RequestException as e:
            print(f"Error: {e}")

    def downloadNews(self):
        """
        Download the xml files and save them in a folder wich name is today's date
        that is within RawData
        """
        todayDate = datetime.today().strftime('%Y-%m-%d')

        folderPath = os.path.join("RawData", todayDate)

        if not os.path.exists(folderPath):
            os.makedirs(folderPath)
            print(f"Folder {folderPath} was created")
        else:
            print("A folder with todays data already exists")

        # Downloading FIles
        for url in self.sectionsUrl:

            fileName = url.split('/')[-1] + ".xml"
            filePath = os.path.join(folderPath, "Expansion - "+fileName)

            response = requests.get(url, headers=self.headers)

            # Saving file
            with open(filePath, "wb") as file:
                file.write(response.content)