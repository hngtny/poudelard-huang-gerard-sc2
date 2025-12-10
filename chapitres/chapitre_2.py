import univers.maison
import utils.input_utils

def rencontrer_amis(joueur):
    print("Vous montez à bord du Poudlard Express. Le train démarre lentement en direction du Nord...)")
    print("Un garçon roux entre dans votre compartiment, l’air amical.")
    reponse_ron = utils.input_utils.demander_choix("— Salut ! Moi c’est Ron Weasley. Tu veux bien qu’on s’assoie ensemble ?", ["Bien sûr, assieds-toi !","Désolé, je préfère voyager seul."])
    if reponse_ron == "Bien sûr, assieds-toi !":
        joueur["Attributs"]["loyauté"]+=1
        print("Ron sourit : — Génial ! Tu verras, Poudlard, c’est incroyable !")
    else:
        joueur["Attributs"]["ambition"]+=1
        print("Ron reste perplexe : Tant pis, j'espère qu'on se recroisera a Poudlard.")

    print("Une fille entre ensuite, portant déjà une pile de livres.")
    reponse_hermione = utils.input_utils.demander_choix("— Bonjour, je m’appelle Hermione Granger. Vous avez déjà lu ‘Histoire de la Magie’ ?", ["Oui, j’adore apprendre de nouvelles choses !","Euh… non, je préfère les aventures aux bouquins."])
    if reponse_hermione == "Oui, j’adore apprendre de nouvelles choses !":
        joueur["Attributs"]["intelligence"]+=1
        print("Hermione sourit : C'est vraiment un superbe livre.")
    else:
        joueur["Attributs"]["courage"]+=1
        print("Hermione fronce les sourcils : — Il faudrait pourtant s’y mettre un jour !")

    print("Puis un garçon blond entre avec un air arrogant.")
    reponse_drago = utils.input_utils.demander_choix("— Je suis Drago Malefoy. Mieux vaut bien choisir ses amis dès le départ, tu ne crois pas ?",["Je lui serre la main poliment.","Je l’ignore complètement.","Je lui réponds avec arrogance."])
    if reponse_drago == "Je lui serre la main poliment.":
        joueur["Attributs"]["ambition"]+=1
        print("Drago vous sourit : Je suis sûr qu'on va très bien s'entendre.")
    elif reponse_drago == "Je l’ignore complètement.":
        joueur["Attributs"]["loyauté"]+=1
        print("Drago fronce les sourcils, vexé. — Tu le regretteras !")
    else:
        joueur["Attributs"]["courage"]+=1
        print("Drago est énernvé : Ne fais pas trop le malin avec moi !")
    print("Tes attributs mis à jour :")
    return joueur["Attributs"]

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

def mot_de_bienvenue():
    print("Bienvenue à Poudlard, je suis le professeur Dumbledore")
    input()

def ceremonie_repartition(joueur):
    questions = [
        (
            "Tu vois un ami en danger. Que fais-tu ?",
            ["Je fonce l'aider", "Je réfléchis à un plan", "Je cherche de l’aide", "Je reste calme et j’observe"],
        ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        ),
        (
            "Quel trait te décrit le mieux ?",
            ["Courageux et loyal", "Rusé et ambitieux", "Patient et travailleur", "Intelligent et curieux"],
             ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        ),
        (
            "Face à un défi difficile, tu...",
            ["Fonces sans hésiter", "Cherches la meilleure stratégie", "Comptes sur tes amis", "Analyses le problème"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        )
    ]
    univers.maison.repartition_maison(joueur, questions)