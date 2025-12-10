def initialiser_personnage(nom,prenom,attributs):
    dico_personnage = {
        "Nom": nom,
        "Prenom": prenom,
        "Argent": 100,
        "Inventaire": [],
        "Sortileges": [],
        "Attributs": attributs,
        "maison": "",
    }
    return dico_personnage

def afficher_personnage(joueur):
    print("Profil du personnage :")

    for cle in joueur:
        valeur = joueur[cle]
        if type(valeur) == dict:
            print(f"{cle} :")
            for sous_cle in valeur:
                print(f" - {sous_cle} : {valeur[sous_cle]}")
        elif type(valeur) == list:
            print(f"{cle} :")
            for element in valeur:
                print("  -", element)
        else:
            print(f"{cle} : {valeur}")


def modifier_argent(joueur,montant):
    joueur["Argent"] += montant
    return joueur


def ajouter_objet(joueur, cle, objet):
    joueur[cle].append(objet)
    return joueur

