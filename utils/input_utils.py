import data
def demander_texte(message):
    texte = str(input(message)).strip()
    while texte == "":
        texte = str(input(message)).strip()
    return message +texte

def demander_nombre(message, min_val=None, max_val=None):
    valid = False

    while valid == False:
        texte = input(message).strip()
        est_entier = True
        negatif = False


        if len(texte) == 0:
            est_entier = False

        i = 0
        if est_entier and texte[0] == '-' and len(texte) > 1:
            negatif = True
            i = 1
        elif est_entier and texte[0] == '-' and len(texte) == 1:
            est_entier = False

        nombre_final = 0
        if est_entier:
            for c in texte[i:]:
                if not (ord('0') <= ord(c) <= ord('9')):
                    est_entier = False
                else:
                    nombre_final = nombre_final * 10 + (ord(c) - ord('0'))

        if est_entier and negatif:
            nombre_final = -nombre_final

        if not est_entier:
            print("Veuillez entrer un nombre entier valide.")
        else:
            hors_bornes = False

            if min_val is not None and nombre_final < min_val:
                hors_bornes = True
            if max_val is not None and nombre_final > max_val:
                hors_bornes = True

            if hors_bornes:
                print(f"Veuillez entrer un nombre entre {min_val} et {max_val}.")
            else:
                valid = True

    return nombre_final


def demander_choix(message, options):
    print(message)
    print()
    for i in range(len(options)):
        print(f"{i+1}. {options[i]}")
    print()
    choix = demander_nombre("Votre choix : ",1,len(options))
    return options[choix-1]

import json

def load_fichier(chemin_fichier):
    with open(chemin_fichier, "r", encoding="utf-8") as fichier:
        donnees = json.load(fichier)
    return donnees

