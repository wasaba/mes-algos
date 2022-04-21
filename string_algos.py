import math


# structure de données: les Tries

class NoeudDuTrie:
    def __init__(self):
        self.children = [None] * 26
        self.finDuMot = False


class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return NoeudDuTrie()

    def lettreAIndice(self, lettre):
        return ord(lettre) - ord('a')

    def inserer(self, key):
        noeudAcc = self.root
        longueur = len(key)

        for level in range(longueur):
            index = self.lettreAIndice(key[level])

            if not noeudAcc.children[index]:
                noeudAcc.children[index] = self.getNode()
            noeudAcc = noeudAcc.children[index]

        noeudAcc.finDuMot = True

    def recherche(self, key):
        noeudAcc = self.root
        longueur = len(key)
        for level in range(longueur):
            index = self.lettreAIndice(key[level])
            if not noeudAcc.children[index]:
                return False
            noeudAcc = noeudAcc.children[index]
        return noeudAcc.finDuMot

    def vide(self, racine):
        for i in range(26):
            if racine.children[i] is not None:
                return False
        return True

    def enlever(self, clé, profondeur, noeud=None):
        racine = self.root if noeud is None else noeud

        if racine is None:
            return None

        if profondeur == len(clé):
            if racine.finDuMot:
                racine.finDuMot = False
            if self.vide(racine):
                racine = None
            return racine

        indice = ord(clé[profondeur]) - ord('a')
        racine.children[indice] = self.enlever(clé, profondeur + 1, racine.children[
            indice])  # veiller ici à l'argument de la fonction récursive

        if self.vide(racine) and not racine.finDuMot:
            racine = None

        return racine


# traitement des chaînes de caractères

# algorithme de Rabin-Karp

d = 100


def search(pat, txt, q):
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0
    t = 0
    h = 1

    for i in range(M - 1):
        h = (h * d) % q

    for i in range(M):
        p = (d * p + ord(pat[i])) % q
        t = (d * t + ord(pat[i])) % q

    for i in range(N - M + 1):
        if p == t:
            for j in range(M):
                if txt[i + j] != pat[j]:
                    break
                else:
                    j += 1

            if j == M:
                print("Pattern à l'indice " + str(i))

        if i < N - M:
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q

            if t < 0:
                t = t + q

# txt = "truc je suis turc avec des trucs"
# pat = "truc"

# q = 101

# search(pat, txt, q)
