from Pr6.labyrinth.maze import graph


class CC:
    def __init__(self, g: graph.Graph):
        self._marked = []
        self._id = []
        self._count = 0
        self._graph = g
        for i in range(0, g.vertices()):
            self._id.append(i)
            self._marked.append(False)
        for i in range(0, g.vertices()):
            if not self._marked[i]:
                self._dfs(i)
                self._count += 1

    def _dfs(self, v):
        self._marked[v] = True
        self._id[v] = self._count
        for w in self._graph.adj(v):
            if not self._marked[w]:
                self._dfs(w)

    def count(self):
        return self._count

    def id(self, v):
        return self._id[v]


def main():
    g = graph.Graph()
    g.add_edge(0, 5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 6)
    g.add_edge(6, 4)
    g.add_edge(4, 3)
    g.add_edge(4, 5)
    g.add_edge(5, 3)
    g.add_edge(7, 8)
    g.add_edge(9, 10)
    g.add_edge(9, 12)
    g.add_edge(9, 11)
    g.add_edge(11, 12)

    print(g)

    cc = CC(g)
    print(f"Count of components: {cc.count()}")
    for i in range(0, g.vertices()):
        print(f"Vertex {i} is in {cc.id(i)} component")


if __name__ == "__main__":
    main()
