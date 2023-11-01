def afficher_triangle(taille):
    for i in range(taille):
        print("*" * (i + 1))


taille = int(input("Entrez la taille du triangle : "))

afficher_triangle(taille)
