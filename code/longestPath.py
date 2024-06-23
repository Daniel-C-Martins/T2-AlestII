from topological import Topological

class LongestPathDAG:
    def __init__(self, graph, s):
        self.graph = graph
        self.s = s
        self.dist_to = {v: -float('inf') for v in graph.getVerts()}
        self.edge_to = {v: None for v in graph.getVerts()}
        self.dist_to[s] = 0
    
    def find_longest_path(self):
        topo_sort = Topological(self.graph).getTopological()
        
        for v in topo_sort:
            if self.dist_to[v] != -float('inf'):
                for w in self.graph.getAdj(v):
                    if w not in self.dist_to:
                        self.dist_to[w] = -float('inf')
                    if self.dist_to[w] < self.dist_to[v] + 1:
                        self.dist_to[w] = self.dist_to[v] + 1
                        self.edge_to[w] = v
    
    def path_to(self, v):
        if v not in self.dist_to or self.dist_to[v] == -float('inf'):
            return None
        path = []
        while v is not None and v != self.s:
            path.insert(0, v)
            v = self.edge_to[v]
        if v is None:
            return None
        path.insert(0, self.s)
        return path
