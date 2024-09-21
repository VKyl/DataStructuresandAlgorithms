import abc


class UF(abc.ABC):

    @abc.abstractmethod
    def union(self, p, q):
        pass

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    @abc.abstractmethod
    def find(self, p):
        pass

    @abc.abstractmethod
    def count(self):
        pass
