import textwrap


def nom_du_mois(mois):
    noms = ["Janvier", "Fevrier", "Mars", "Avril",
            "Mai", "Juin", "Juillet", "Août",
            "Septembre", "Octobre", "Novembre", "Décembre"];

    if mois < 1 or mois > 12:
        return "ERREUR: Numéro de mois incorrect " + mois

    return noms[mois - 1]


def afficher_titre(mois, annee):
    print("============================")
    print("      ", nom_du_mois(mois), " ", str(annee))
    print("============================")


def afficher_en_tete():
    print("Lu  Ma  Me  Je  Ve  Sa  Di")


def est_bissextile(annee):
    if annee % 4 == 0:
        if annee % 100 == 0:
            if annee % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def nombre_de_jours(mois, annee):
    if mois == 1 or mois == 3 or mois == 5 or mois == 7 or mois == 8 or mois == 10 or mois == 12:
        return "31"
    elif mois == 4 or mois == 6 or mois == 9 or mois == 11:
        return "30"
    elif mois == 2:
        if est_bissextile(annee):
            return "29"
        else:
            return "28"
    else:
        return "erreur, numéro de mois incorrect " + mois


def suite_numeros_jours(mois, annee):
    n_de_jours = nombre_de_jours(mois, annee)
    numero_jour_1 = numero_jour(1, mois, annee)

    suite = "    " * numero_jour_1
    for i in range(1, int(n_de_jours) + 1):
        suite = suite + "{:02d}".format(i) + "  "

    return suite


def numero_jour(jour, mois, annee):
    # formula zeller
    q = jour
    m = mois
    if mois < 3:
        m = mois + 12
        annee = annee - 1
    j = annee // 100
    k = annee % 100

    # formule de la congruence de Zeller
    h = (q + ((m + 1) * 13 // 5) + k + (k // 4) + (j // 4) + 5 * j + 5) % 7
    return h


def afficher_calendrier(mois, annee):
    afficher_titre(mois, annee)
    afficher_en_tete()
    output = textwrap.wrap(suite_numeros_jours(mois, annee), 28)
    for ligne in output:
        print(ligne)
