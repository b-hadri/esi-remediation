def afficher_triangle_sur_pointe_de(taille):
    for i in range(1, taille + 1):
        print("* " * (taille + 1 - i));


def main():
    taille = int(input("Entrez la taille du triangle sur pointe: "))
    afficher_triangle_sur_pointe_de(taille)


main()
