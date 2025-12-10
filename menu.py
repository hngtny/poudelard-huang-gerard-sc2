import chapitres
import utils

def afficher_menu_principal():
    print("1. Lancer le Chapitre 1 – L’arrivée dans le monde magique.")
    print("2. Quitter le jeu.")

def lancer_choix_menu():
    maisons = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0
    }
    afficher_menu_principal()
    choix = demander_choix("Votre choix :",["1","2"])
    if choix == "1":
        joueur = lancer_chapitre_1()
        maison = lancer_chapitre_2(joueur)
        lancer_chapitre_3(joueur, maison)

    elif choix == "2":
        print("Merci d'avoir joué ! À bientôt.")
        break

    else:
        print("Choix invalide. Veuillez saisir 1 ou 2.")