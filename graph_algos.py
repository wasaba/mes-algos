import math
from collections import defaultdict


# algorithmes sur les graphes

# Parcours basiques

class Graphe:
    def __init__(self):
        self.graphe = defaultdict(list)

    def AjoutNoeud(self, u, v):
        self.graphe[u].append(v)
        self.graphe[v].append(u)

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

    # trouver des élements connectés

    def UtilitaireDFS(self, temporaire, noeud, visité):
        visité[noeud] = True
        temporaire.append(noeud)

        for i in self.graphe[noeud]:
            if not visité[i]:
                temp = self.UtilitaireDFS(temporaire, i, visité)

        return temporaire

    def connectedComponents(self):
        visités = []
        cc = []
        for i in self.graphe:
            visités.append(False)

        for i in self.graphe:
            if not visités[i]:
                cc.append(self.UtilitaireDFS([], i, visités))
        return cc

monGraphe = Graphe()

monGraphe.AjoutNoeud(1, 0)
monGraphe.AjoutNoeud(2, 3)
monGraphe.AjoutNoeud(3, 4)

print(monGraphe.connectedComponents())
