import calendrier


def afficher_les_dates_de_l_annee(annee):
    for numero_mois in range(1, 13):
        nombre_jours_mois = calendrier.nombre_de_jours(numero_mois, annee)
        for numero_jour in range(1, int(nombre_jours_mois) + 1):
            print("{:02d}/{:02d}/{:4d}".format(numero_jour, numero_mois, annee))


afficher_les_dates_de_l_annee(2023)
