import math


# algèbre

def binaryExponentiation(numA, numB):
    if numB == 0:
        return 1;
    res = binaryExponentiation(numA, numB // 2)
    if numB % 2:
        return res * res * numA
    else:
        return res * res


def exponentiationMudolate(numA, numB, modulo):
    numA = numA % modulo
    res = 1
    while numB > 0:
        if (numB % 1):
            res = res * numA % modulo
        numA = numA * numA % modulo
        numB >>= 1
    return res


# structures de données

def ConstructionSparseTable(arr, n):
    for i in range(n):
        vision[i][0] = arr[i]

    j = 1

    while (1 << j) <= n:
        i = 0
        while (i + (1 << j) - 1) < n:

            if vision[i][j - 1] < vision[i + (1 << (j - 1))][j - 1]:
                vision[i][j] = vision[i][j - 1]
            else:
                vision[i][j] = vision[i + (1 << (j - 1))][j - 1]

            i += 1
        j += 1


def requête(L, R):
    j = int(math.log2(R - L + 1))

    if vision[L][j] <= vision[R - (1 << j) + 1][j]:
        return vision[L][j]
    else:
        return vision[R - (1 << j) + 1][j]


a = [7, 2, 3, 0, 5, 10, 3, 12, 18]
n = len(a)
MAX = 500
vision = [[0 for i in range(MAX)] for j in range(MAX)]

ConstructionSparseTable(a, n)

# décomposition en racine carrée

MAXN = 10000
SQRSIZE = 100

arr = [0] * (MAXN)
block = [0] * (SQRSIZE)
blk_sz = 0


def update(idx, val):
    blockNumber = idx // blk_sz
    block[blockNumber] += val - arr[idx]
    arr[idx] = val


def query(l, r):
    sum = 0
    while (l < r and l % blk_sz != 0 and l != 0):
        sum += arr[l]
        l += 1

    while l + blk_sz <= r:
        sum += block[l // blk_sz]
        l += blk_sz

    while l <= r:
        sum += arr[l]
        l += 1

    return sum


def preprocess(inp, n):
    blk_idx = -1

    global blk_sz
    blk_sz = int(math.sqrt(n))
    for i in range(n):
        arr[i] = inp[i]
        if i % blk_sz == 0:
            blk_idx += 1

        block[blk_idx] += arr[i]


inp = [1, 5, 2, 4, 6, 1, 3, 5, 7, 10]
n = len(inp)


# preprocess(inp, n)
# print(query(3,8))
# print(query(1,6))
# update(8, 0)
# print(query(8,8))

# structure de données: les Tries

class NoeudDuTrie:
    def __init_(self):
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

t = Trie()



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

txt = "truc je suis turc avec des trucs"
pat = "truc"

q = 101

search(pat, txt, q)
