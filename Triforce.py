print("Dessiner une Triforce")
SYM_ESPACE = "."
SYM_ETOILE = "*"

# Demande de taille
taille = int(input("Taille : "))
while taille < 2:
    taille = int(input("Erreur : "))

# Dessin
nb_espace = taille * 2 - 1
nb_etoile = 1
while nb_espace >= 0:
    # if nb_etoile > taille * 2 - 1:
    #     nb_etoile = 1
    nb_etoile = nb_etoile % (taille * 2)

    espace = ""
    for i in range(0, nb_espace):
        espace += SYM_ESPACE

    etoile = ""
    for i in range(0, nb_etoile):
        etoile += SYM_ETOILE

    if nb_espace >= taille:
        print(espace,etoile, sep="")
    else :
        espace_int = espace + SYM_ESPACE + espace
        print(espace, etoile, espace_int, etoile, sep="")

    nb_espace = nb_espace - 1
    nb_etoile = nb_etoile + 2