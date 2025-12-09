def initialiser_personnage(nom,prenom,attributs):
    dico_personnage = {
        "Nom": nom,
        "Prenom": prenom,
        "Argent": 100,
        "Inventaire": [],
        "Sortileges": [],
        "Attributs": attributs
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


personnage = {
    "Nom": "Potter",
    "Prénom": "Harry",
    "Argent": 100,
    "Inventaire": [],
    "Sortilèges": [],
    "Attributs": {
        "courage": 8,
        "intelligence": 8,
        "loyauté": 8,
        "ambition": 8
    }
}



def modifier_argent(joueur,montant):
    joueur["Argent"] += montant
    return joueur


def ajouter_objet(joueur, cle, objet):
    joueur[cle].append(objet)
    return joueur

