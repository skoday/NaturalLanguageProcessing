from scraping import LaJornada

sections = ['Deportes', 'Economía', 'Ciencias', 'Cultura']

new_object = LaJornada()

new_object.getSectionsUrl(sections=sections)

new_object.downloadNews()