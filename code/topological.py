from digraph import Digraph


class Topological:
    def __init__(self, g):
        self.marked = {}
        self.verts = []
        for v in g.getVerts():
            if v not in self.marked:
                self.__dfs(g, v)

    def getTopological(self):
        return self.verts

    def __dfs(self, g, s):
        self.marked[s] = True
        for w in g.getAdj(s):
            if w not in self.marked:
                self.__dfs(g, w)
        self.verts.insert(0, s)


if __name__ == "__main__":

    g = Digraph("tinydag.txt")

    topo = Topological(g)

    for v in topo.getTopological():
        print(f"{v} ", end="")
    print()
