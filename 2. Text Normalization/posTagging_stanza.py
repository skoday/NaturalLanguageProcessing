#Importamos la biblioteca stanza
import stanza

#Se carga el modelo en español
# ~ stanza.download ('es')

cadena = "Juan estaba corriendo por el pasillo de la ESCOM."
# ~ cadena = "Juan estaba corriendo por el pasillo de Microsoft. "
# ~ cadena = "Los perros ladraron la otra noche a unos coches rojos que pasaron por la calle."

nlp = stanza.Pipeline('es')

#Se realiza el análisis de la cadena
doc = nlp(cadena)


for sent in doc.sentences:
	print ('Oración: ', sent.text)
	
	for token in sent.words:
		# ~ print(token.text, token.pos_, token.lemma_)
		print(token.text, token.lemma, token.pos, token.deprel)
		# ~ print(token.text, token.pos_, token.dep_, token.lemma_, spacy.explain(token.tag_), spacy.explain(token.dep_))
# ~ displacy.serve(doc, style="dep")    

for entity in doc.ents:
    print(entity.text, entity.type)
