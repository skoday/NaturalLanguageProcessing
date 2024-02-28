#Importamos la biblioteca spacy
import spacy
from spacy import displacy
#conda install -c conda-forge spacy-model-es_core_news_sm
#python -m spacy download es_core_news_sm

cadena = "Juan estaba corriendo por el pasillo de la Escuela Superior de Cómputo."
# ~ cadena = "Juan estaba corriendo por el pasillo de Microsoft. "
# ~ cadena = "Juan vive en la Ciudad de México. "
# ~ cadena = "Los perros ladraron la otra noche a unos coches rojos que pasaron por la calle."

#Se carga el corpus para el tagger en español
nlp = spacy.load("es_core_news_sm")
#Se realiza el análisis de la cadena
doc = nlp(cadena)

for token in doc:
    # ~ print(token.text, token.pos_, token.lemma_)
    # ~ print(token.text, token.pos_, token.dep_, token.lemma_)
    print(token.text, token.pos_, token.dep_, token.lemma_, spacy.explain(token.tag_), spacy.explain(token.dep_))
# ~ displacy.serve(doc, style="dep")    

for entity in doc.ents:
    print(entity.text, entity.label_)
