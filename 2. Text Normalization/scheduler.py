from scraper import LaJornada, Expansion
from consolidation import Consolidation
from datetime import datetime
from normalization import Normalization

class Run:
    def __init__(self) -> None:
        self.sections = ['Deportes', 'Economía', 'Ciencias', 'Cultura']
        self.today = datetime.now()
        self.start = 4
        self.end = 8

        if self.today.month == 3 and self.start <= self.today.day <= self.end:
            new_object = LaJornada()
            new_object.getSectionsUrl(sections=self.sections)
            new_object.downloadNews()
            expansion = Expansion()
            expansion.getSectionsUrl()
            expansion.downloadNews()

        if self.today.month == 3 and self.today.day == self.end:
            consolidation = Consolidation()
            consolidation.consolidate()
            normalization = Normalization()
            normalization.normalize()