import math

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