def exercice1():
    n = int(input('Entrez un entier [0 .. 20] : '))
    while not (0 <= n <= 20):
        n = int(input('Entrez un entier [0 .. 20], S.V.P. : '))


def exercice2():
    n = int(input('Entrez un entier [0 .. 20] : '))
    while not (0 <= n <= 20):
        n = int(input('Entrez un entier [0 .. 20], S.V.P. : '))
    if n < 10:
        print("Insuffissant")
    elif 10 <= n < 12:
        print("Passable")
    elif 12 <= n < 14:
        print("AB")
    elif 14 <= n < 16:
        print("B")
    elif n >= 16:
        print("TB")


def exercice3():
    somme = 0
    min = 20
    max = 0
    recu = ""
    for i in range(10):
        nom_etudiant = str(input('Entrez un nom d\'étudiant : '))
        note_etudiant = int(input('Entrez un entier [0 .. 20] : '))
        while not (0 <= note_etudiant <= 20):
            note_etudiant = int(input('Entrez un entier [0 .. 20], S.V.P. : '))
        somme += note_etudiant
        if note_etudiant > max:
            max = note_etudiant
        if note_etudiant < min:
            min = note_etudiant
        if note_etudiant >= 10:
            recu += nom_etudiant + " "
    print("la moyenne est : ", somme / 10)
    print("les reçus sont : ", recu)


def exercice4():
    somme = 0
    nb_recu = 0
    tableau = []
    noteSupMoy = ""
    for i in range(10):
        note_etudiant = int(input('Entrez un entier [0 .. 20] : '))
        while not (0 <= note_etudiant <= 20):
            note_etudiant = int(input('Entrez un entier [0 .. 20], S.V.P. : '))
        tableau.append(note_etudiant)
        somme += note_etudiant
        if note_etudiant >= 10:
            nb_recu += 1
    moyenne = somme / 10
    print("la moyenne est : ", moyenne)
    print("le nombre de reçus est : ", nb_recu)
    for i in range(0, 10):
        if tableau[i] >= moyenne:
            noteSupMoy += str(i) + " "
    print("les indices des étudiants reçus sont : ", noteSupMoy)


def exercice5():
    somme = 0
    nb = int(input('Entrez un entier positif : '))
    while not (nb > 0):
        nb = int(input('Entrez un entier positif : '))
    if nb % 2 == 0:
        while nb != 0:
            nb -= 2
            somme += nb
    else:
        nb -= 1
        while nb != 0:
            somme += nb
            nb -= 2
    print(somme)


def exercice6():
    borneInf = int(input('Entrez une borne inf : '))
    borneSup = int(input('Entrez une borne sup : '))
    pas = int(input('Entrez un pas : '))
    for i in range(borneInf, borneSup + 1, pas):
        fonction = (2 * (i ** 3)) + i - 5
        print("le pas est : ", i, "la fonction vaut :", fonction)


def exercice7():
    tableau = [-566, -67890, 12, 0]
    print(tableau)
    for i in range(len(tableau)):
        actuel = tableau[i]
        j = i
        while j > 0 and tableau[j - 1] > actuel:
            tableau[j] = tableau[j - 1]
            j -= 1
            tableau[j] = actuel
    print(tableau)


if __name__ == '__main__':
    print("-------------- EXERCICE 1")
    # exercice1()
    print("-------------- EXERCICE 2")
    # exercice2()
    print("-------------- EXERCICE 3")
    # exercice3()
    print("-------------- EXERCICE 4")
    # exercice4()
    print("-------------- EXERCICE 5")
    # exercice5()
    print("-------------- EXERCICE 6")
    # exercice6()
    print("-------------- EXERCICE 7")
    exercice7()
