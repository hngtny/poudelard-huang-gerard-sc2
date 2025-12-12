import utils.input_utils
import univers.personnage
from utils.input_utils import load_fichier


def introduction():
    print("Bienvenue dans cette nouvelle aventure jeune sorcier !")
    print("L'étrange grimoire s'illumine dans vos mains...")
    print("Votre histoire commence maintenant...")
    print()
    input("Appuyez sur une touche pour continuer...")


def creer_personnage():
    nom = input("Entrez le nom de votre personnage : ")
    while nom == "":
        nom = input("Entrez le nom de votre personnage : ")
    prenom = input("Entrez le prénom de votre personnage : ")
    while prenom == "":
        prenom = input("Entrez le prénom de votre personnage : ")

    print("Choisissez vos attributs :")

    attributs = {
        "courage": utils.input_utils.demander_nombre("Niveau de courage (1,10) :",1,10),
        "intelligence": utils.input_utils.demander_nombre("Niveau d'intelligence (1,10) :",1,10),
        "loyauté": utils.input_utils.demander_nombre("Niveau de loyauté (1,10) :",1,10),
        "ambition": utils.input_utils.demander_nombre("Niveau d'ambition (1,10) :",1,10),
    }

    joueur = univers.personnage.initialiser_personnage(nom, prenom, attributs)
    univers.personnage.afficher_personnage(joueur)
    return joueur


def recevoir_lettre():
    print("Une chouette traverse la fenêtre et vous apporte une lettre scellée")
    print("du sceau de Poudlard...")
    print("« Cher élève,")
    print("Nous avons le plaisir de vous informer que vous avez été admis à")
    print("l’école de sorcellerie de Poudlard ! »")
    print()
    print("Souhaitez-vous accepter cette invitation et partir pour Poudlard ?")

    choix = utils.input_utils.demander_choix("Votre choix :",["Oui, bien sûr !","Non, je préfère travailler mon algèbre"])
    if choix=="Non, je préfère travailler mon algèbre":
        print("Vous déchirez la lettre, Le prof de Mathématique pousse un cri de joie:")
        print("« EXCELLENT ! Enfin quelqu’un de passionné par les nombres complexes dans cette école ! »")
        print("Le monde magique ne saura jamais que vous existiez... Fin du jeu.")
        exit(0)
    else:
        print("Vous acceptez l’invitation. Votre aventure magique commence...")

def rencontrer_hagrid(personnage):
    print(f"Hagrid : 'Salut {personnage["Prenom"]} ! Je suis venu t’aider à faire tes achats sur")
    print("le Chemin de Traverse.'")

    choix = utils.input_utils.demander_choix("Voulez-vous suivre Hagrid",[" Oui"," Non"])

    if choix == "1":
        print("Vous décidez de suivre Hagrid.")
    else:
        print("Hagrid vous attrape par le col puis vous met dans sa poche. ")

    print("Vous partez tous les deux en direction du Chemin de Traverse...")

def acheter_fournitures(personnage):
    catalogue = load_fichier("data/inventaire.json")

    obligatoires = ["Baguette magique", "Robe de sorcier", "Manuel de potions"]
    animaux = {
        "1": ("Chouette", 20),
        "2": ("Chat", 15),
        "3": ("Rat", 10),
        "4": ("Crapaud", 5)
    }

    print("Bienvenue sur le Chemin de Traverse !")
    print("Catalogue des objets disponibles :")
    for k, v in catalogue.items():
        print(f"{k}. {v[0]} - {v[1]} galions")

    argent = personnage["Argent"]
    inventaire = personnage["Inventaire"]

    print(f"Vous avez {argent} galions.")

    while obligatoires:
        print("Objets obligatoires restant à acheter :", ", ".join(obligatoires))
        choix = input("Entrez le numéro de l'objet à acheter : ")

        if choix not in catalogue:
            print("Choix invalide.")
            continue

        nom, prix = catalogue[choix]

        if prix > argent:
            print("Vous n'avez pas assez d'argent. Vous perdez la partie.")
            exit(0)

        inventaire.append(nom)
        argent -= prix
        print(f"Vous avez acheté : {nom} (-{prix} galions).")
        print(f"Vous avez {argent} galions.")

        if nom in obligatoires:
            obligatoires.remove(nom)

    print("Tous les objets obligatoires ont été achetés !")
    print("Il est temps de choisir votre animal de compagnie pour Poudlard !")
    print(f"Vous avez {argent} galions.")
    print("Voici les animaux disponibles :")
    for k, v in animaux.items():
        print(f"{k}. {v[0]} - {v[1]} galions")

    while True:
        choix_animal = input("Votre choix : ")

        if choix_animal in animaux:
            break
        else:
            print("Choix invalide. Veuillez saisir un numéro d’animal.")

    animal, prix = animaux[choix_animal]

    if prix > argent:
        print("Vous n'avez pas assez d'argent. Vous perdez la partie.")
        exit(0)

    inventaire.append(animal)
    argent -= prix

    personnage["inventaire"] = inventaire
    personnage["Argent"] = argent

    print(f"Vous avez choisi : {animal} (-{prix} galions).")
    print("Tous les objets obligatoires ont été achetés avec succès ! Voici votre inventaire final :")
    print("Profil du personnage :")
    print(f"Nom : {personnage['Nom']}")
    print(f"Prenom : {personnage['Prenom']}")
    print(f"Argent : {personnage['Argent']}")
    print("Inventaire :", ", ".join(personnage["Inventaire"]))

    print("Sortilèges :")
    for s in personnage["Sortileges"]:
        print("-", s)

    print("Attributs :")
    for k, v in personnage["Attributs"].items():
        print(f"- {k} : {v}")

def lancer_chapitre_1():
    introduction()
    joueur = creer_personnage()
    recevoir_lettre()
    rencontrer_hagrid(joueur)
    acheter_fournitures(joueur)
    print("Fin du Chapitre 1 ! Votre aventure commence a Poudlard !!!")
    return joueur
