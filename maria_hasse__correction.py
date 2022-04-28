import copy

def mult(a, b):
    return a + b

def add(a, b):
    return a if a < b else b

def element_produit(M1, M2, i, j):
    cumul = float("inf")
    for k in range(len(M1)):
        cumul = add(cumul, mult(M1[i][k], M2[k][j]))
    return cumul

def produit(M1, M2):
    matrice_produit = [[0] * len(M1) for _ in range(len(M2))]
    for i in range(len(M1)):
        for j in range(len(M1)):
            matrice_produit[i][j] = element_produit(M1, M2, i, j)
    return matrice_produit


def maria_hasse(M):
    C = copy.deepcopy(M)
    P = produit(M, C)
    k = 1
    while P != M:
        M = copy.deepcopy(P)
        P = produit(M, C)
        #print(M)
        k += 1
    return k


inf = float("inf")
C = [[0, 8, inf, inf, 4, inf],
     [inf, 0, 3, inf, 8, inf],
     [inf, inf, 0, 2, inf, inf],
     [13, 3, inf, 0, inf, 5],
     [inf, inf, inf, 5, 0, inf],
     [1, inf, inf, inf, 6, 0]]

maria_hasse(C)
