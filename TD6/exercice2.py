def lancer_2des_n(n):
    de1 = []
    de2 = []
    compteur = 0
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == n and i <= j:
                de1.append(i)
                de2.append(j)
                compteur += 1
    print("Dé 1 prend les valeurs : ", de1)
    print("Dé 2 prend les valeurs : ", de2)
    print("Il y a ", compteur, "façons d'obtenir ", n)

def lancer_3des_n(n):
    de1 = []
    de2 = []
    de3 = []
    compteur = 0
    for i in range(1, 7):
        for j in range(1, 7):
            for h in range(1, 7):
                if i + j + h == n and i <= j <= h:
                    de1.append(i)
                    de2.append(j)
                    de3.append(h)
                    compteur += 1
    print("Dé 1 prend les valeurs : ", de1)
    print("Dé 2 prend les valeurs : ", de2)
    print("Dé 3 prend les valeurs : ", de3)
    print("Il y a ", compteur, "façons d'obtenir ", n)
    
if __name__ == '__main__':
    lancer_2des_n(8)
    lancer_2des_n(12)
    lancer_2des_n(1)
    lancer_2des_n(6)
    lancer_3des_n(3)
    lancer_3des_n(6)
    lancer_3des_n(18)