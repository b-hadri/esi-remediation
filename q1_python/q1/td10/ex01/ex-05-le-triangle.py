def afficher_triangle_de(taille):
    for i in range(1, taille+1):
        print("* "*i);


def main():
    taille = int(input("Entrez la taille du triangle : "))
    afficher_triangle_de(taille)


main()
