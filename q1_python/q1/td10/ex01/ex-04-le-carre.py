def afficher_carre_de(taille):
    for i in range(taille):
        for j in range(taille):
            print("* ", end="")
        print("");


def main():
    taille = int(input("Entrez la taille du carré : "))
    afficher_carre_de(taille)


main()
