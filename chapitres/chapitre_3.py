import random
import univers.personnage
import univers.maison
from univers.maison import actualiser_points_maison, afficher_maison_gagnante
from univers.personnage import afficher_personnage
from utils.input_utils import load_fichier


def apprendre_sorts(joueur, chemin_fichier="data/sorts.json"):
    liste_sorts = load_fichier(chemin_fichier)

    offensifs = [s for s in liste_sorts if s["type"].lower() == "offensif"]
    defensifs = [s for s in liste_sorts if s["type"].lower() == "défensif"]
    utilitaires = [s for s in liste_sorts if s["type"].lower() == "utilitaire"]

    sorts_appris = []
    sorts_appris.append(random.choice(offensifs))
    sorts_appris.append(random.choice(defensifs))
    sorts_appris.extend(random.sample(utilitaires, 3))

    print("Tu commences tes cours de magie à Poudlard...")

    for sort in sorts_appris:
        joueur["Sortileges"].append(sort["nom"])
        print(f"Tu viens d'apprendre le sortilège : {sort['nom']} ({sort['type']})")
        input("Appuie sur Entrée pour continuer...")

    print("Tu as terminé ton apprentissage de base à Poudlard !")
    print("Voici les sortilèges que tu maîtrises désormais :")

    for sort in sorts_appris:
        print(f"- {sort['nom']} ({sort['type']}) : {sort['description']}")

def quiz_magie(joueur, chemin_fichier="data/quiz_magie.json"):
    questions = load_fichier(chemin_fichier)

    selection = []
    while len(selection) < 4:
        q = random.choice(questions)
        if q not in selection:
            selection.append(q)

    score = 0

    print("Bienvenue au quiz de magie de Poudlard !")
    print("Réponds correctement aux 4 questions pour faire gagner des points à ta maison.")

    for i, q in enumerate(selection, 1):
        print(f"{i}. {q['question']}")
        reponse = input("> ")

        if reponse.strip().lower() == q["reponse"].lower():
            print("Bonne réponse ! +25 points pour ta maison.")
            score += 25
        else:
            print(f"Mauvaise réponse. La bonne réponse était : {q['reponse']}")

    print(f"Score obtenu : {score} points")
    return score

def lancer_chapitre_3(joueur,maison):
    apprendre_sorts(joueur)
    point = quiz_magie(joueur)
    actualiser_points_maison(univers.maison.maisons, maison, point)
    afficher_maison_gagnante(univers.maison.maisons)
    afficher_personnage(joueur)

