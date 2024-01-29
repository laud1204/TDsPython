def premier_plateau(tableau):
    longueur = 1
    i = 1
    tab = tableau[0]
    while i < len(tableau):
        if tab == tableau[i]:
            longueur += 1
        else:
            return tab, longueur
        i += 1
    return tab, longueur


def nb_plateaux(tableau):
    nbPlateau = 1
    longueur = 1
    i = 1
    tab = tableau[0]
    while i < len(tableau):
        if tab == tableau[i]:
            longueur += 1
            tab = tableau[i]
        else:
            nbPlateau += 1
            tab = tableau[i]
            longueur = 1
        i += 1
    return nbPlateau


def plus_long(tableau):
    longueur = 1
    i = 1
    plusGdeLongueur = longueur
    while i < len(tableau):
        if tableau[i] == tableau[i-1]:
            longueur += 1
        else:
            if plusGdeLongueur < longueur:
                plusGdeLongueur = longueur
            longueur = 1
        i += 1
    if longueur > plusGdeLongueur:
        plusGdeLongueur = longueur
    return plusGdeLongueur


def nombre_max(tableau):
    plusLong = plus_long(tableau)
    longueur = 1
    i = 1
    nb_max = 0
    while i < len(tableau):
        if tableau[i] == tableau[i - 1]:
            longueur += 1
        else:
            if plusLong == longueur:
                nb_max += 1
            longueur = 1
        i += 1
    if plusLong == longueur:
        nb_max += 1
    return plusLong, nb_max


def coder(tableau):
    new_tableau = []
    while len(tableau) > 0:
        premierPlateau = premier_plateau(tableau)
        new_tableau.append(premierPlateau)
        tableau = tableau[premierPlateau[1]:]
    return new_tableau


def decoder(tableau_compresse):
    new_tableau = []
    for i in tableau_compresse:
        for j in range(i[1]):
            new_tableau.append(i[0])
    return new_tableau