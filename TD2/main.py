def exercice1(phrase):
    for caractere in phrase:
        print(caractere)


def exercice2(liste):
    for element in liste:
        print(element)


def exercice3():
    nb = str(input('Entrez un nombre, ou une suite de caractères : '))
    if nb == nb[::-1]:
        print('Oui, "',nb,'" est un palindrome')
    else:
        print('Non, "',nb,'"n\'est pas un palindrome')


def exercice4(v):
    if v <= 100000:
        nb = 0
        for j in range(v, 0, -1):
            somme = 0
            produit = 1
            for i in str(j):
                somme += int(i)
                produit = produit * int(i)
            if somme == produit:
                nb += 1
        print("le nombre de nombres vérifiant la condition est ", nb)
    else:
        print("V donné est trop grand")


def exercice5_valide(chaineADN):
    valide = True
    for c in chaineADN:
        if c != 'a' and c != 't' and c != 'g' and c != 'c':
            valide = False
    return valide


def exercice5_chaine(chaine, sequence):
    return sequence in chaine


def exercice5_final():
    chaine = str(input('Entrez une chaine : '))
    sequence = str(input('Entrez une séquence : '))
    if exercice5_valide(chaine) and exercice5_valide(sequence) and exercice5_chaine(chaine, sequence):
        print("La chaine et la séquence sont valides et la séquence est contenue dans la chaîne")
    else:
        if exercice5_valide(chaine) and exercice5_valide(sequence) and not exercice5_chaine(chaine, sequence):
            print("La chaine et la séquence sont valides mais la séquence n'est pas contenue dans la chaîne")
        else:
            if exercice5_valide(chaine) and not exercice5_valide(sequence):
                print("la chaine est valide mais pas la séquence")
            else:
                if exercice5_valide(sequence) and not exercice5_valide(chaine):
                    print("la séquence est valide mais pas la chaine")
                else:
                    print("rien n'est valide")

if __name__ == '__main__':
    print("-------------- EXERCICE 1")
    exercice1("voici une phrase")
    print("-------------- EXERCICE 2")
    exercice2([3, -5, 78, -90])
    print("-------------- EXERCICE 3")
    exercice3()
    print("-------------- EXERCICE 4")
    exercice4(100000)
    print("-------------- EXERCICE 5 - 1")
    print(exercice5_valide("azerty"))
    print(exercice5_valide("agtc"))
    print(exercice5_valide("ag tc"))
    print("-------------- EXERCICE 5 - 2")
    print(exercice5_chaine('il fait beau', 'fai'))
    print(exercice5_chaine('il fait beau', 'soleil'))
    print("-------------- EXERCICE 5 - 3")
    exercice5_final()