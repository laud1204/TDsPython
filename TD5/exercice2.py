def trier(tableau):
    for e in tableau:
        if e != "bleu" and e != "blanc" and e != "rouge":
            print("Tableau incorrect")

    gauche = 0
    droite = len(tableau) - 1
    milieu = 0

    while milieu <= droite:
        if tableau[milieu] == "bleu":
            tableau[gauche], tableau[milieu] = tableau[milieu], tableau[gauche]
            gauche += 1
            milieu += 1
        else:
            if tableau[milieu] == "rouge":
                tableau[milieu], tableau[droite] = tableau[droite], tableau[milieu]
                droite -= 1
            else:
                milieu += 1
    return tableau
