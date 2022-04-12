import math
from collections import defaultdict


# algorithmes sur les graphes

# Parcours basiques

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Breadth First Search (méthode itérative)
    def BFS(self, s):
        visited = [s]

        queue = [s]

        while queue:
            f = queue.pop()
            print(f)
            for i in self.graph[f]:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)

    # Depth First Search (méthode récursive)
    def DFS(self, s, visited=set()):
        visited.add(s)
        print(s, end=" ")
        for neighbour in self.graph[s]:
            if neighbour not in visited:
                self.DFS(neighbour, visited)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is DFS from (starting from vertex 2)")
g.DFS(2)
