import utils.input_utils

def rencontrer_amis(joueur):
    reponse_ron = utils.input_utils.demander_choix("— Salut ! Moi c’est Ron Weasley. Tu veux bien qu’on s’assoie ensemble ?", ["Bien sûr, assieds-toi !","Désolé, je préfère voyager seul."])
    if reponse_ron == "Bien sûr, assieds-toi !":
        joueur["Attributs"]["loyauté"]+=1
    else:
        joueur["Attributs"]["ambition"]+=1
    reponse_hermione = utils.input_utils.demander_choix("— Bonjour, je m’appelle Hermione Granger. Vous avez déjà lu ‘Histoire de la Magie’ ?", ["Oui, j’adore apprendre de nouvelles choses !","Euh… non, je préfère les aventures aux bouquins."])
    if reponse_hermione == "Oui, j’adore apprendre de nouvelles choses !":
        joueur["Attributs"]["intelligence"]+=1
    else:
        joueur["Attributs"]["courage"]+=1
    reponse_drago = utils.input_utils.demander_choix("— Je suis Drago Malefoy. Mieux vaut bien choisir ses amis dès le départ, tu ne crois pas ?",["Je lui serre la main poliment.","Je l’ignore complètement.","Je lui réponds avec arrogance."])
    if reponse_drago == "Je lui serre la main poliment.":
        joueur["Attributs"]["ambition"]+=1
    elif reponse_drago == "Je l’ignore complètement.":
        joueur["Attributs"]["loyauté"]+=1
    else:
        joueur["Attributs"]["courage"]+=1
    return joueur

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


