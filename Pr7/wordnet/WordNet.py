from Input import read_file
from Synset import Synset
from Digraph import DiGraph


class WordNet:
    def __init__(self, synset_fname: str, hypernyms_fname: str, fdata_path: str = None):
        self._graph = DiGraph()
        self._synsets = list(read_file(synset_fname, path=fdata_path,
                                       parser=lambda x: Synset(*x.split(",", maxsplit=2))))
        self._hypernyms = list(read_file(hypernyms_fname, path=fdata_path,
                                         parser=lambda x: x.replace("\n", "").split(",")))
        self._nouns = []

        for hypernym in self._hypernyms:
            if len(hypernym) > 1:
                for synset in hypernym[1:]:
                    self._graph.add_edge(int(hypernym[0]), int(synset))
            else:
                self._graph.add_edge(int(hypernym[0]), int(hypernym[0]))

    @property
    def synsets(self):
        return self._synsets.copy()

    @property
    def hypernyms(self):
        return self._hypernyms.copy()

    @property
    def nouns(self) -> list:
        if not self._nouns:
            res = set()
            for synset in self._synsets:
                res.update(synset.nouns)
            self._nouns = sorted(list(res))
        return self._nouns

    def is_noun(self, word: str) -> bool:
        word = word.replace(" ", "_")
        left = 0
        right = len(self.nouns) - 1
        while left <= right:
            mid = (left + right) // 2
            if word == self.nouns[mid]:
                return True
            if word < self.nouns[mid]:
                right = mid - 1
            if word > self.nouns[mid]:
                left = mid + 1
        return False

    def distance(self, noun: str, other_noun: str) -> int:
        if not_noun1 := not self.is_noun(noun) or not self.is_noun(other_noun):
            raise ValueError(f"{noun if not_noun1 else other_noun} is not a noun")
        return sum(self._find(noun, other_noun)[:2]) - 1

    def sap(self, noun: str, other_noun: str) -> tuple:
        if not self.is_noun(noun) or not self.is_noun(other_noun):
            raise ValueError("Both words must be valid nouns.")
        return self._synsets[self._find(noun, other_noun)[2]].synset

    def _find(self, noun: str, other_noun: str) -> tuple:
        if noun == other_noun:
            noun_id = list(self._get_synset_id(noun))
            return 0, 0, noun_id[0]

        noun_ids = list(self._get_synset_id(noun))
        other_noun_ids = list(self._get_synset_id(other_noun))

        visited = {}

        self._look_up(noun_ids[0], visited)
        ancestor_id, dist1, dist2 = self._look_up(other_noun_ids[0], visited)

        for noun_id in noun_ids:
            for other_noun_id in other_noun_ids:
                visited = {}
                self._look_up(noun_id, visited)
                ancestor_id, dist1, dist2 = min([self._look_up(other_noun_id, visited), (dist1, dist2, ancestor_id)],
                                                key=lambda x: x[1] + x[2])
        return dist1, dist2, ancestor_id

    def _get_synset_id(self, noun: str):
        noun = noun.replace(" ", "_")
        for synset in self._synsets:
            for syn_noun in synset.nouns:
                if noun == syn_noun:
                    yield synset.id
        return None

    def _look_up(self, starting_id, visited: dict):
        visited = visited
        queue = [starting_id]
        dist = 0
        while queue:
            current = queue.pop(0)
            if visited and current in visited.keys():
                dist2 = visited[current]
                return current, dist, dist2
            dist += 1
            visited[current] = dist
            queue.extend(self._graph.adj(current))
        return -1, 1, len(self._synsets)


if __name__ == '__main__':
    wordnet = WordNet('synsets.txt', 'hypernyms.txt', './data')
    # Ya loh, pomilka cherez lowercase sliv 🤡
    # noun1 = wordnet.synsets[21012].nouns[0]
    # noun2 = wordnet.synsets[56099].nouns[0]
    # noun1 = wordnet.synsets[0].nouns[0]
    # noun2 = wordnet.synsets[79541].nouns[0]
    # noun1 = "domestic_dog"
    # noun2 = "true_cat"
    noun1 = "true_cat"
    noun2 = "domestic_dog"

    try:
        distance = wordnet.distance(noun1, noun2)
        ancestor = wordnet.sap(noun1, noun2)
        print(f"Distance from {noun1} to {noun2}: {distance}")
        print(f"Ancestor between {noun1} and {noun2}: {ancestor}")
    except ValueError as e:
        print(e)
