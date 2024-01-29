def chaine_valide(chaineADN):
    valide = True
    for c in chaineADN:
        if c != 'a' and c != 't' and c != 'g' and c != 'c':
            valide = False
    return valide


def chaine_in_sequence(chaine, sequence):
    return sequence in chaine


def nb_occurence(chaine, sequence):
    if chaine_in_sequence(chaine, sequence):
        return chaine.count(sequence)


if __name__ == '__main__':
    chaine = str(input('Entrez une chaine : '))
    sequence = str(input('Entrez une séquence : '))
    if chaine_valide(chaine) and chaine_valide(sequence) and chaine_in_sequence(chaine, sequence):
        print("Le nombre d'occurrence de la chaîne dans la séquence est : ", nb_occurence(chaine,sequence))