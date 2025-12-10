maisons = {
 "Gryffondor": 0,
 "Serpentard": 0,
 "Poufsouffle": 0,
 "Serdaigle": 0
}
def actualiser_points_maison(maisons, nom_maison, points):
    if nom_maison not in maisons:
        print("La maison est introuvable ")
    else:
        maisons[nom_maison] += points
        print(f"La maison {nom_maison} reçoit {points} points")
    return maisons

def afficher_maison_gagnante(maisons):
    score_max = None
    for score in maisons.values():
        if score_max is None or score > score_max:
            score_max = score
    gagnants = []
    for maison, score in maisons.items():
        if score == score_max:
            gagnants.append(maison)
    if len(gagnants) == 1:
        print(f"La maison gagnante est : {gagnants} avec {score_max} points")
    else:
        print(f"Les maisons gagnantes sont : {gagnants}, avec {score_max} points")


def repartition_maison(joueur, questions):
    scores = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0
        }

    scores["Gryffondor"] += joueur["Attributs"]["courage"] * 2
    scores["Serpentard"] += joueur["Attributs"]["ambition"] * 2
    scores["Poufsouffle"] += joueur["Attributs"]["loyauté"] * 2
    scores["Serdaigle"] += joueur["Attributs"]["intelligence"] * 2

    for question, choix, maisons_associees in questions:
        print(question)
        i = 1
        for option in choix:
            print(str(i) + ". " + option)
            i += 1
        reponse = int(input("Ton choix : "))
        maison = maisons_associees[reponse - 1]
        scores[maison] += 3
        print()

    maison_gagnante = None
    meilleur_score = None
    for maison, score in scores.items():
        if meilleur_score is None or score > meilleur_score:
            meilleur_score = score
            maison_gagnante = maison

    return maison_gagnante

