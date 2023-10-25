def exercice1(adresse_ip):
    valide = True
    for element in adresse_ip.split("."):
        if not 0 <= int(element) <= 255:
            valide = False
    return valide


def exercice2(adresse_ip):
    binaire = ""
    # on vérifie que l'ip soit valide
    if exercice1(adresse_ip):
        for element in adresse_ip.split("."):
            element = int(element)
            for i in range(7, -1, -1):
                if int(element) >= 2**i:
                    element -= 2**i
                    binaire += "1"
                else:
                    binaire += "0"
    else:
        print("Adresse IP non valide")
    return binaire

def exercice3(adresse_ip, masque, adresse_reseau):
    # Si adresse_ip, masque et adresse_reseau sont valides
    if exercice1(adresse_ip) and exercice1(masque) and exercice1(adresse_reseau):
        return exercice2(adresse_reseau) == exercice3_etLogique(exercice2(adresse_ip), exercice2(masque))
    else:
        print("Une des adresses est invalide")


def exercice3_etLogique(binaire1, binaire2):
    masque = ""
    for b1, b2 in zip(binaire1, binaire2):
        if b1 == b2 == "1":
            masque += "1"
        else :
            masque += "0"
    return masque


def ouLogique(binaire1, binaire2):
    masque = ""
    for b1, b2 in zip(binaire1, binaire2):
        if (b1 == "1" and b2 == "0") or (b1 == "0" and b2 == "1") or (b1 == "1" and b2 == "1"):
            masque += "1"
        else :
            masque += "0"
    return masque


def exercice4(masque):
    compteur = 0
    for element in exercice2(masque):
        if element == "0":
            compteur += 1
    return 2**compteur - 2

def exercice4_compteur(masque):
    compteur = 0
    for element in exercice2(masque):
        if element == "0":
            compteur += 1
    return compteur

def exercice5(adresse_ip, masque):
    binaire_adresse_reseau = exercice3_etLogique(exercice2(adresse_ip), exercice2(masque))
    print("L'adresse réseau est : ", exercice5_binaireVersIP(binaire_adresse_reseau))
    print("La première adresse valable est : ", exercice5_binaireVersIP(ouLogique(binaire_adresse_reseau, "00000000000000000000000000000001")))
    derniere_adresse = ""
    for i in range(32):
        if i == 31:
            derniere_adresse += "0"
        elif i < 32 - exercice4_compteur(masque):
            derniere_adresse += "0"
        else:
            derniere_adresse += "1"
    print("La dernière adresse valable est : ",
          exercice5_binaireVersIP(ouLogique(binaire_adresse_reseau, derniere_adresse)))
    adresse_diffusion = ""
    for i in range(32):
        if i < 32-exercice4_compteur(masque):
            adresse_diffusion += "0"
        else:
            adresse_diffusion += "1"
    print("L'adresse de diffusion valable est : ", exercice5_binaireVersIP(ouLogique(binaire_adresse_reseau, adresse_diffusion)))



def exercice5_binaireVersIP(binaire):
    ip = ""
    nb = 0
    j = 0
    liste_paquet = [binaire[0:8], binaire[8:16], binaire[16:24], binaire[24:32]]
    for element in liste_paquet:
        i = 8
        nb = 0
        for e in element:
            i -= 1
            if e == "1":
                nb += 2**i
        j += 1
        if j < 4:
            ip += str(nb)
            ip += "."
        else :
            ip += str(nb)
    return ip


if __name__ == '__main__':
    print("-------------- EXERCICE 1")
    print("Affichera false si IP pas valide, sinon True")
    print(exercice1("5.10.222.189"))
    print(exercice1("256.-12.900.800"))
    print("-------------- EXERCICE 2")
    print(exercice2("192.168.5.2"))
    print(exercice2("256.-12.900.800"))
    print("-------------- EXERCICE 3")
    print(exercice3("192.168.100.3", "255.255.255.0", "192.168.100.0"))
    print("-------------- EXERCICE 4")
    print("Il peut y avoir ", exercice4("255.255.255.0"), " adresses disponibles")
    print("Il peut y avoir ", exercice4("255.255.0.0"), " adresses disponibles")
    print("Il peut y avoir ", exercice4("255.255.255.250"), " adresses disponibles")
    print("-------------- EXERCICE 5")
    print(exercice5("192.168.5.0", "255.255.255.0"))


