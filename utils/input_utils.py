def demander_texte(message):
    texte = str(input(message)).strip()
    while texte == "":
        texte = str(input(message)).strip()
    return message +texte

def demander_nombre(message,min_val=None,max_val=None):
    nombre = str(input(message))
    #on doit verifier si l'utilisateur rentre un nombre et convertir si c'est un str
    if min_val==None and max_val==None:
        return message + str(nombre)
    while nombre < min_val or nombre > max_val:
        nombre=int(input(f"Veuillez entrer un nombre entre {min_val} et {max_val}"))
    return message + str(nombre)

def demander_choix(message,options):
    choix=str(input(message))


