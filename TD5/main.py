import exercice1, exercice2


if __name__ == '__main__':
    tab = [7,7,7,7,7,5,5,5,5,1,1,3,3,1,2,2,4,4,4,5,5,5,5,5]
    tab2 = ['rouge', 'bleu', 'blanc', 'rouge', 'bleu', 'blanc']
    print("-------------- EXERCICE 1 - 1")
    print(exercice1.premier_plateau(tab))
    print("-------------- EXERCICE 1 - 2")
    print(exercice1.nb_plateaux(tab))
    print("-------------- EXERCICE 1 - 3")
    print(exercice1.plus_long(tab))
    print("-------------- EXERCICE 1 - 4")
    print(exercice1.nombre_max(tab))
    print("-------------- EXERCICE 1 - 5")
    print(exercice1.coder(tab))
    print("-------------- EXERCICE 1 - 6")
    print(exercice1.decoder([[7,5],[5,4],[1,2],[3,2],[1,1],[2,2],[4,3],[5,5]]))
    print("-------------- EXERCICE 2 - 1")
    print(exercice2.trier(tab2))
