class Synset:
    def __init__(self, w_id: int, synset: str, desc: str):
        self._id: int = int(w_id)
        self._synset: str = synset
        self._desc:str = desc

    @property
    def id(self):
        return self._id

    @property
    def synset(self):
        return self._synset

    @property
    def desc(self):
        return self._desc

    @property
    def nouns(self):
        return self._synset.split()

    def index(self, noun):
        return self.nouns.index(noun)

    def __eq__(self, other: str):
        return other.replace(" ", "_") in self.synset

    def __iter__(self):
        return self.nouns.__iter__()

    def __str__(self):
        return f'{self._id},{self.synset},{self.desc}'

    def __repr__(self):
        return str(self)
