import univers.personnage

def introduction():
    print("Bienvenue dans cette nouvelle aventure jeune sorcier !")
    print("L'étrange grimoire s'illumine dans vos mains...")
    print("Votre histoire commence maintenant...")
    print()
    input("Appuyez sur une touche pour continuer...")
introduction()
def creer_personnage():
    nom = input("Entrez le nom de votre personnage : ")
    prenom = input("Entrez le prénom de votre personnage : ")

    print("Choisissez vos attributs :")

    def demander_attribut(texte):
        valeur = 0
        while valeur < 1 or valeur > 10:
            try:
                valeur = int(input(f"{texte} (1-10) : "))
            except ValueError:
                valeur = 0
        return valeur

    attributs = {
        "courage": demander_attribut("Niveau de courage"),
        "intelligence": demander_attribut("Niveau d’intelligence"),
        "loyauté": demander_attribut("Niveau de loyauté"),
        "ambition": demander_attribut("Niveau d’ambition")
    }

    joueur = univers.personnage.initialiser_personnage(nom, prenom, attributs)
    univers.personnage.afficher_personnage(joueur)
    return joueur
creer_personnage()
def recevoir_lettre():
    print("Une chouette traverse la fenêtre et vous apporte une lettre scellée")
    print("du sceau de Poudlard...")
    print("« Cher élève,")
    print("Nous avons le plaisir de vous informer que vous avez été admis à")
    print("l’école de sorcellerie de Poudlard ! »")
    print()
    print("Souhaitez-vous accepter cette invitation et partir pour Poudlard ?")
    print("1. Oui, bien sûr !")
    print("2. Non, je préfère travailler mon algèbre")

    choix = ""
    while choix not in ("1", "2"):
        choix = input("Votre choix : ")

    if choix == "2":
        print("Vous déchirez la lettre, Le prof de Mathématique pousse un cri de joie:")
        print("« EXCELLENT ! Enfin quelqu’un de passionné par les nombres complexes dans cette école ! »")
        print("Le monde magique ne saura jamais que vous existiez... Fin du jeu.")
        exit(0)

    print("Vous acceptez l’invitation. Votre aventure magique commence...")
def rencontrer_hagrid(personnage):
    print(f"Hagrid : 'Salut {personnage.prenom} ! Je suis venu t’aider à faire tes achats sur")
    print("le Chemin de Traverse.'")
    print("Voulez-vous suivre Hagrid ?")
    print("1. Oui")
    print("2. Non")

    choix = ""
    while choix not in ("1", "2"):
        choix = input("Votre choix : ")

    if choix == "1":
        print("Vous décidez de suivre Hagrid.")
    else:
        print("Hagrid vous attrape par le col puis vous met dans sa poche. ")

    print("Vous partez tous les deux en direction du Chemin de Traverse...")
