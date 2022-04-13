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