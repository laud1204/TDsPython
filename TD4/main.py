import math
import string


class Cle:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def alphabet():
    return list(string.ascii_lowercase)


def exercice1_1_cleValide(cle):
    return math.gcd(cle.a, 26) == 1


def rang_vers_lettre(rang):
    return chr(ord("a") + rang)


def lettre_vers_rang(lettre):
    return ord(lettre) - ord("a")


def exercice1_2_chiffrement(texte, cle):
    texte_code = ""
    if exercice1_1_cleValide(cle):
        for l in texte:
            y = (lettre_vers_rang(l) * cle.a + cle.b) % 26
            texte_code += rang_vers_lettre(y)
    return texte_code


def exercice1_3_dechiffrement(cle):
    for i in range(26):
        if (cle.a * i) % 26 == 1:
            return Cle(i, cle.b)


def exercice1_4_crypto(crytogramme, cle_dechiffrement):
    texte_decode = ""
    for l in crytogramme:
        x = (cle_dechiffrement.a * (lettre_vers_rang(l) - cle_dechiffrement.b)) % 26
        texte_decode += rang_vers_lettre(x)
    return texte_decode


def manipulation_cle(texte, cle):
    cle_repetee = ""
    for i in range(len(texte) // len(cle)):
        cle_repetee += cle
    for i in range(len(texte) % len(cle)):
        cle_repetee += cle[:i]
    return cle_repetee


def exercice2_1_cryptage(texte, cle):
    cle_repetee = manipulation_cle(texte, cle)
    print("Texte à coder :", texte)
    print("Clé de chiffrement :", cle_repetee)
    texte_crypte = ""
    for l1, l2 in zip(texte, cle_repetee):
        texte_crypte += rang_vers_lettre((lettre_vers_rang(l1) + lettre_vers_rang(l2)) % 26)
    print("Texte crypté :", texte_crypte)


def exercice2_2_dechiffrement(texte_code, cle):
    cle_repetee = manipulation_cle(texte_code, cle)
    print("Texte à décoder :", texte_code)
    print("Clé de chiffrement :", cle_repetee)
    texte_decrypte = ""
    for l1, l2 in zip(texte_code, cle_repetee):
        texte_decrypte += rang_vers_lettre((lettre_vers_rang(l1) - lettre_vers_rang(l2)) % 26)
    print("Texte décrypté :", texte_decrypte)


if __name__ == '__main__':
    print("-------------- EXERCICE 1 - 1")
    cle1 = Cle(3, 10)
    print(exercice1_1_cleValide(cle1))
    cle2 = Cle(20, -10)
    print(exercice1_1_cleValide(cle2))
    print("-------------- EXERCICE 1 - 2")
    print(exercice1_2_chiffrement("bonjour", cle1))
    print("-------------- EXERCICE 1 - 3")
    print(exercice1_3_dechiffrement(cle1).a, exercice1_3_dechiffrement(cle1).b)
    print("-------------- EXERCICE 1 - 4")
    print(exercice1_4_crypto("naxlasj", Cle(9, 10)))
    print("-------------- EXERCICE 2 - 1")
    exercice2_1_cryptage("thisisatestmessage", "sesame")
    print("-------------- EXERCICE 2 - 2")
    exercice2_2_dechiffrement("llasuwsxwsfqwwkasi", "sesame")
