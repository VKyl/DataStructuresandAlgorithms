import graph


class DFS:
    def __init__(self, g: graph.Graph, source: int):
        self._graph = g
        self._source = source
        self._edge_to = []
        self._marked = []
        for _ in range(0, g.vertices()):
            self._edge_to.append(None)
            self._marked.append(False)
        self._dfs(source)

    def _dfs(self, v):
        self._marked[v] = True
        stack = [v]
        while len(stack) > 0:
            x = stack.pop()
            for w in self._graph.adj(x):
                if not self._marked[w]:
                    stack.append(w)
                    self._marked[w] = True
                    self._edge_to[w] = x

    def has_path_to(self, v):
        return self._marked[v]

    def path_to(self, v):
        if not self.has_path_to(v):
            return None
        path = []
        x = v
        while x != self._source:
            path.insert(0, x)
            x = self._edge_to[x]
        path.insert(0, self._source)
        return path


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

    print(g)

    source = 0
    dfs = DFS(g, source)
    for i in range(0, g.vertices()):
        if dfs.has_path_to(i):
            print(dfs.path_to(i))
        else:
            print(f"{source} not connected with {i}")


if __name__ == "__main__":
    main()
