import calendrier


def main():
    mois = 10  # int(input("Numéro de mois : "))
    annee = 2023  # int(input("Numéro de l'année : "))

    calendrier.afficher_calendrier(mois, annee)
    calendrier.afficher_calendrier(mois + 1, annee)
    calendrier.afficher_calendrier(mois + 2, annee)
    calendrier.afficher_calendrier(1, annee + 1)
    calendrier.afficher_calendrier(2, annee + 1)



main()
