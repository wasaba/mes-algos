import math

# Combinatoire

# trouver la plus grande puissance tel que k^x | n!

def puissance(n, k):
    reste = 0
    while n:
        n = n // k
        reste += n
    return reste


# calculer coefficient binomial (algorithme récursif de base en O(n*max(n-1,k))

def C(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1

    return C(n - 1, k - 1) + C(n - 1, k)


# nombres de Catalan

def catalan(n):
    return int((1 / (n + 1) * C(2 * n, n)))
