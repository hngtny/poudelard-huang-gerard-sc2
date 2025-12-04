def initialiser_personnage(nom,prenom,attributs):
    dictionnaire_personnage = {}
    dictionnaire_personnage["Nom"] = nom
    dictionnaire_personnage["Prenom"] = prenom
    dictionnaire_personnage["Argent"] = 100
    dictionnaire_personnage["Inventaire"] = []
    dictionnaire_personnage["Sortilèges"] = []
    dictionnaire_personnage["Attributs"] = attributs
    return dictionnaire_personnage

def afficher_personnage(joueur):
    print("Profil du personnage :")
    print("Nom :", joueur.keys("nom"))
    print("Prenom :", joueur.prenom)
    print("Argent :", joueur.argent)
    print("Inventaire :", joueur.inventaire)
    print("Sortilèges :", joueur.sortilèges)
    if isinstance(valeur, dict):
        print(titre)
        for sous_cle, sous_valeur in valeur.items():
            print(f"- {sous_cle} : {sous_valeur}")


personnage = {
    "nom": "Potter",
    "prenom": "Harry",
    "argent": 100,
    "inventaire": [],
    "sortilèges": [],
    "attributs": {
        "courage": 8,
        "intelligence": 8,
        "loyauté": 8,
        "ambition": 8
    }
}

afficher_personnage(personnage)