from scraper import LaJornada, Expansion

sections = ['Deportes', 'Economía', 'Ciencias', 'Cultura']
new_object = LaJornada()
new_object.getSectionsUrl(sections=sections)
new_object.downloadNews()

expansion = Expansion()
expansion.getSectionsUrl()
expansion.downloadNews()