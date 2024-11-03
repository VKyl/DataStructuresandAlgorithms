from WordNet import WordNet
from WordNet import read_file


class Outcast:
    def __init__(self, WordNet):
        self._wordNet = WordNet

    def outcast(self, nouns: list[str]):
        max_dist = 0
        outcast_noun = nouns[0]
        for i, word1 in enumerate(nouns[0:]):
            distance = 0
            for word2 in nouns:
                dist = self._wordNet.distance(word1, word2)
                distance += dist
            if distance > max_dist:
                max_dist = distance
                outcast_noun = word1
        return outcast_noun


if __name__ == '__main__':
    wordnet = WordNet('synsets.txt', 'hypernyms.txt', './data')
    outcast = Outcast(wordnet)
    nouns = str(list(read_file("outcast5.txt", "./data"))[0]).split()
    try:
        outcast = outcast.outcast(nouns)
        print(f"Outcasted element: {outcast}")
    except ValueError as e:
        print(e)

