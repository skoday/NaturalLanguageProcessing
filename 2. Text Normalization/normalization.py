import os
import spacy
import pandas as pd

class Normalization:

    def __init__(self) -> None:
        self.file_name = "raw_data_corpus.csv"
        self.path = "Normalization process"
        self.nlp = spacy.load("es_core_news_sm")
        self.stopwords = ["DET", "ADP", "CCONJ", "PRON"]

    def fileExists(self):
        return os.path.exists(self.file_name)

    def readFile(self):
        return pd.read_csv(self.file_name)
        
    def writeFile(self, data, name):
        data.to_csv(name, index=False)

    def normalize(self):
        if not self.fileExists():
            return print("No such file exists.\nBye Bye")

        data = self.readFile()
        data["Título"] = data["Título"].apply(self.nlp)
        data["Contenido"] = data["Contenido"].apply(self.nlp)

        def traverse_entity(doc):
            result = []
            for item in doc:
                if item.pos_ not in self.stopwords:
                    result.append(item.lemma_)
            return result

        data["Título"] = data["Título"].apply(traverse_entity)
        data["Contenido"] = data["Contenido"].apply(traverse_entity)

        self.writeFile(data, "normalized data corpus.csv")