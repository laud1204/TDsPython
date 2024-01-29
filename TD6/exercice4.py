import os


def compte_lignes(nom_fichier):
    if os.path.exists(nom_fichier):
        with open(nom_fichier, 'r') as fp:
            lines = len(fp.readlines())
            print('Nombre de lignes : ', lines)
    else:
        print("Le chemin spécifié n'existe pas.")


if __name__ == '__main__':
    compte_lignes("test.txt")
    print("")
    compte_lignes('test2.txt')
