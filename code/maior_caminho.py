from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def longest_path_util(self, v, visited, path):
        visited[v] = True
        path.append(v)

        longest_path = list(path)

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                current_path = self.longest_path_util(neighbor, visited, path)
                if len(current_path) > len(longest_path):
                    longest_path = current_path

        path.pop()
        visited[v] = False
        return longest_path
    
    def find_longest_path(self):
        all_vertices = set(self.graph.keys())
        for neighbors in self.graph.values():
            all_vertices.update(neighbors)
        
        visited = {v: False for v in all_vertices}
        longest_path = []

        for vertex in all_vertices:
            current_path = self.longest_path_util(vertex, visited, [])
            if len(current_path) > len(longest_path):
                longest_path = current_path

        return longest_path

def read_graph_from_file(file_path):
    edges = []
    with open(file_path, 'r') as file:
        for line in file:
            u, v = map(int, line.split())
            edges.append((u, v))
    return edges

# Caminho do arquivo que contém as arestas
file_path = 'Resultados\\grafo.txt'

# Lendo as arestas do arquivo
edges = read_graph_from_file(file_path)

# Criando o grafo
g = Graph()

for u, v in edges:
    g.add_edge(u, v)

# Encontrando e imprimindo o maior caminho
longest_path = g.find_longest_path()
print("O maior caminho no dígrafo é:", longest_path)