def inserer(fichier, position, ligne):
    with open(fichier, 'r+') as f1:
        list_lignes = f1.readlines()
        list_lignes.insert(position, ligne)
        f1.writelines(list_lignes)
    return list_lignes

if __name__ == '__main__':
    print(inserer("test2.txt", 5, "AAAAAAAAA"))