class Employe:
    def __init__(self):
        nom = ""
        prenom = ""
        salaire = 0
        anciennete = 0


def saisie_employe():
    print("Saisir un employé : ")
    employe = Employe()
    employe.nom = str(input('Entrez un nom : '))
    employe.prenom = str(input('Entrez un prénom : '))
    employe.salaire = int(input('Entrez un salaire : '))
    employe.anciennete = int(input('Entrez une ancienneté : '))
    return employe


def majoration_prime_4ans(bases_employes):
    for e1 in bases_employes:
        if e1.anciennete > 4:
            augmentation = e1.salaire * (2*(10**(-2)))
            e1.salaire += augmentation + 200


def creer_bases(taille):
    bases_employes = []
    while taille != len(bases_employes):
        bases_employes.append(saisie_employe())
    return bases_employes


if __name__ == '__main__':
    taille = int(input('Vous voulez créer une base de combien d\'employés ? '))
    base = creer_bases(taille)
    majoration_prime_4ans(base)
    for element in base:
        print(element.nom, element.prenom, element.salaire, element.anciennete)