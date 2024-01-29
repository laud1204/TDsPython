import numpy as np


def matrice_nXn(n):
    matrice =[]
    for i in range(n):
        ligne = []
        for j in range(n):
            ligne.append(2**j)
        matrice.append(ligne)
    return matrice

def matrice_diagonale(n):
    matrice = []
    diag = 0
    for i in range(n):
        ligne = []
        for j in range(n):
            if j == diag:
                ligne.append(1)
            else:
                ligne.append(0)
        diag += 1
        matrice.append(ligne)
    return matrice


def calculer_M3(matrice1, matrice2, n):
    matrice = []
    for i in range(n):
        ligne = []
        for j in range(n):
            matrice1[i][j] *= 5
            matrice2[i][j] *= 2
            ligne.append(matrice1[i][j]-matrice2[i][j])
        matrice.append(ligne)
    return matrice


if __name__ == '__main__':
    print(matrice_nXn(3))
    print("")
    print(matrice_diagonale(6))
    print("")
    print(calculer_M3(matrice_nXn(3), matrice_diagonale(3), 3))