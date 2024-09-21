from . import uf


class WeightedQuickUnion(uf.UF):
    def __init__(self, number_of_elements):
        elements_range = range(number_of_elements)
        self._elements = list(elements_range)
        self._size = [1] * number_of_elements
        self._count = number_of_elements

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)

        if p_root == q_root:
            return

        if self._size[p_root] <= self._size[q_root]:
            self._elements[p_root] = q_root
            self._size[q_root] += self._size[p_root]
        else:
            self._elements[q_root] = p_root
            self._size[p_root] += self._size[q_root]

        self._count -= 1

    def find(self, p):
        while p != self._elements[p]:
            p = self._elements[p]

        return p

    def count(self):
        return self._count

    def __repr__(self):
        return str(self._elements)
