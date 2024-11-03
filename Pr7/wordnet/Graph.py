class Graph:
    def __init__(self):
        self._vertex_count = 0
        self._edges_count = 0
        self._adj = []

    def vertices(self):
        return self._vertex_count

    def edges(self):
        return self._edges_count

    def add_edge(self, v, w):
        if len(self._adj) <= v or len(self._adj) <= w:
            self._extend(max(v, w))
        if not w in self._adj[v]:
            self._adj[v].append(w)
        if not v in self._adj[w]:
            self._adj[w].append(v)
        self._edges_count += 1

    def _extend(self, v):
        while len(self._adj) <= v:
            self._adj.append([])
        self._vertex_count = len(self._adj)

    def degree(self, v):
        if v >= len(self._adj):
            return -1
        return len(self._adj[v])

    def adj(self, v):
        return self._adj[v]

    def __str__(self):
        res = ""
        res += str(self._vertex_count) + " vertices, " + str(
            self._edges_count) + " edges \n"
        i = 0
        for v in self._adj:
            res += str(i) + ": "
            res += str(v)
            res += "\n"
            i += 1
        return res


def main():
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 5)
    g.add_edge(0, 6)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    g.add_edge(3, 5)
    g.add_edge(4, 5)
    g.add_edge(4, 6)
    g.add_edge(7, 8)
    g.add_edge(9, 10)
    g.add_edge(9, 11)
    g.add_edge(9, 12)
    g.add_edge(11, 12)
    print(f"degree 0: {g.degree(0)}")
    print(g)


if __name__ == "__main__":
    main()

