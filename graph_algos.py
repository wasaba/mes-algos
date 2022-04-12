import math
from collections import defaultdict


# algorithmes sur les graphes

# Parcours basiques

class Graphe:
    def __init__(self):
        self.graphe = defaultdict(list)

    def AjoutNoeud(self, u, v):
        self.graphe[u].append(v)

    # Breadth First Search (méthode itérative)
    def BFS(self, s):
        visite = [s]

        queue = [s]

        while queue:
            f = queue.pop()
            print(f)
            for i in self.graphe[f]:
                if i not in visite:
                    queue.append(i)
                    visite.append(i)

    # Depth First Search (méthode récursive)

    def DFS(self, s, visite=set()):
        visite.add(s)
        print(s, end=" ")
        for voisin in self.graphe[s]:
            if voisin not in visite:
                self.DFS(voisin, visite)


monGraphe = Graphe()

monGraphe.AjoutNoeud(0, 1)
monGraphe.AjoutNoeud(0, 2)
monGraphe.AjoutNoeud(1, 2)
monGraphe.AjoutNoeud(2, 0)
monGraphe.AjoutNoeud(2, 3)
monGraphe.AjoutNoeud(3, 3)

monGraphe.DFS(2)
