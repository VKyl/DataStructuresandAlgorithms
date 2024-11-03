class DiGraph:
    def __init__(self):
        self._vertex_count = 0
        self._edges_count = 0
        self._adj = []

    def vertex_count(self):
        return self._vertex_count

    def edges_count(self):
        return self._edges_count

    def add_edge(self, v, w):
        if len(self._adj) <= v:
            self._extend(v)
        if not w in self._adj[v]:
            self._adj[v].append(w)
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
        res += str(self._vertex_count) + " vertices, " + str(self._edges_count) + " edges \n"
        i = 0
        for v in self._adj:
            res += str(i) + ": "
            res += str(v)
            res += "\n"
            i += 1
        return res


if __name__ == "__main__":
    graph = DiGraph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 5)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 5)
    graph.add_edge(3, 2)
    graph.add_edge(4, 3)
    graph.add_edge(4, 2)
    graph.add_edge(5, 4)
    graph.add_edge(6, 8)
    graph.add_edge(6, 9)
    graph.add_edge(7, 6)
    graph.add_edge(8, 6)
    graph.add_edge(9, 10)
    graph.add_edge(9, 11)
    graph.add_edge(10, 12)
    graph.add_edge(11, 12)
    graph.add_edge(12, 9)
    print(f'degree 0: {graph.degree(0)}')
    print(graph)
