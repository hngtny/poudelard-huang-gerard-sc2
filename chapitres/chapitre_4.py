import random
import json

def creer_equipe(maison,equipe_data,est_joueur=False,joueur=None):
    equipe = {
        'nom': maison,
        "score": 0,
        "a_marque": 0,
        "a_stoppe": 0,
        "attrzpe_vifdor": False,
        "joueurs": equipe_data['joueurs'],
    }
    if est_joueur and joueur != None:
        nouveaux_joueurs = []
        joueur_principal = f"{joueur['Nom']} {joueur['Prenom']} (Attrapeur)"
        nouveaux_joueurs.append(joueur_principal)

        for j in equipe_data['joueurs']:
            if joueur["Nom"] not in j and joueur["Prenom"] not in j:
                nouveaux_joueurs.append(j)

        equipe["joueurs"] = nouveaux_joueurs

    return equipe

def tentative_marque(equipe_attaque, equipe_defense, joueur_est_joueur=False):
    proba_but = random.randint(1, 10)

    if proba_but >= 6:
        if joueur_est_joueur:
            buteur = equipe_attaque["joueurs"][0]
        else:
            buteur = random.choice(equipe_attaque["joueurs"][1:])

        equipe_attaque["score"] += 10
        equipe_attaque["a_marque"] += 1

        print(f"{buteur} marque un but pour {equipe_attaque['nom']} ! (+10 points)")
    else:
        equipe_defense["a_stoppe"] += 1
        print(f"{equipe_defense['nom']} bloque l'attaque !")

def attraper_vifdor(e1, e2):
    gagnant = random.choice([e1, e2])
    gagnant["score"] += 150
    gagnant["attrape_vifdor"] = True
    print(f"Le Vif d’Or a été attrapé par {gagnant['nom']} ! (+150 points)")
    return gagnant

def afficher_score(e1, e2):
    print("Score actuel :")
    print(f"→ {e1['nom']} : {e1['score']} points")
    print(f"→ {e2['nom']} : {e2['score']} points")

def afficher_equipe(maison, equipe):
    print(f"Équipe de {maison} :")
    for j in equipe["joueurs"]:
        print(f"- {j}")


def apparition_vifdor():
    return random.randint(1, 10) == 1


def match_quidditch(joueur, maisons):
    with open("data/equipes_quidditch.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    maison_joueur = joueur["maison"]
    adversaires = [m for m in data.keys() if m != maison_joueur]
    maison_adverse = random.choice(adversaires)

    equipe_joueur = creer_equipe(maison_joueur, data[maison_joueur], est_joueur=True, joueur=joueur)
    equipe_adverse = creer_equipe(maison_adverse, data[maison_adverse])

    print(f"Match de Quidditch : {maison_joueur} vs {maison_adverse} !")

    afficher_equipe(maison_joueur, equipe_joueur)
    afficher_equipe(maison_adverse, equipe_adverse)

    print(f"Tu joues pour {maison_joueur} en tant qu’Attrapeur")
    input()

    for tour in range(1, 21):
        print(f"━━━ Tour {tour} ━━━")

        tentative_marque(equipe_joueur, equipe_adverse, joueur_est_joueur=True)
        tentative_marque(equipe_adverse, equipe_joueur, joueur_est_joueur=False)

        afficher_score(equipe_joueur, equipe_adverse)

        if apparition_vifdor():
            gagnant = attraper_vifdor(equipe_joueur, equipe_adverse)
            break

        input("Appuyez sur Entrée pour continuer")

    print("Fin du match !")
    afficher_score(equipe_joueur, equipe_adverse)

    if equipe_joueur["score"] > equipe_adverse["score"]:
        gagnant = equipe_joueur
    elif equipe_adverse["score"] > equipe_joueur["score"]:
        gagnant = equipe_adverse
    else:
        print("Match nul !")
        return

    points = 500
    maisons[gagnant["nom"]] += points

    print(f"La maison gagnante est {gagnant['nom']} avec {gagnant['score']} points !")
    print(f"+{points} points pour {gagnant['nom']} ! Total : {maisons[gagnant['nom']]} points.")

def lancer_chapitre4_quidditch(joueur, maisons):
    print("━━━ Chapitre 4 : Le Match de Quidditch ━━━")
    match_quidditch(joueur, maisons)
    print("Fin du Chapitre 4 — Quelle performance incroyable sur le terrain !")
    print("Voici vos informations complètes :")
    print(f"Nom : {joueur['Nom']}")
    print(f"Prenom : {joueur['Prenom']}")
    print(f"Maison : {joueur['maison']}")
    print("Attributs :")
    for k, v in joueur["Attributs"].items():
        print(f"- {k} : {v}")
    print("Inventaire :")
    for item in joueur["Inventaire"]:
        print(f"- {item}")

