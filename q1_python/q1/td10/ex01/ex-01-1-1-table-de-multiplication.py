def afficher_table_de_multiplication(du_nombre, au_nombre):
    for i in range(du_nombre, au_nombre + 1):
        for j in range(1, 11):
            print("{:2d} * {:2d} = {:2d}".format(j, i, j * i))


afficher_table_de_multiplication(2, 10)
