def analyser_2_fichiers(fichier1, fichier2):
    with open(fichier1, 'r') as f1:
        fic1 = f1.read().replace("\n", " ").split(" ")
    with open(fichier2, 'r') as f2:
        fic2 = f2.read().replace("\n", " ").split(" ")
    liste = []
    for l1 in fic1:
        for l2 in fic2:
            if l1 == l2 and l1 not in liste:
                liste.append(l1)
    return liste



if __name__ == '__main__':
    print(analyser_2_fichiers("test.txt", "test2.txt"))
