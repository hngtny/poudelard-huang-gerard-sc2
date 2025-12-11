
from chapitres.chapitre_1 import lancer_chapitre_1
from chapitres.chapitre_2 import lancer_chapitre_2
from chapitres.chapitre_3 import lancer_chapitre_3
from utils.input_utils import demander_choix


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
    choix = input("Votre choix : ")
    while choix!="1" and choix!="2":
        print("Choix invalide. Veuillez saisir 1 ou 2.")
        choix = input("Votre choix : ")

    if choix == "1":
        joueur = lancer_chapitre_1()
        lancer_chapitre_2(joueur)
        maison_joueur = joueur["maison"]
        lancer_chapitre_3(joueur, maison_joueur)

    elif choix == "2":
        print("Merci d'avoir joué ! À bientôt.")
        exit(0)
