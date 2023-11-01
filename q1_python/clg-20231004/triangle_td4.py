# triangles possibles

bool = True;
a = int(input("Entrez un premier nombre : "))
b = int(input("Entrez un second nombre : "))
c = int(input("Entrez un troisième nombre : "))

print("utiliser le théorème d'inégalité")

# https://fr.wikihow.com/savoir-si-trois-longueurs-forment-un-triangle-valide
# 1) cas ou c'est OK
# Entrez un premier nombre : 7
# Entrez un second nombre : 10
# Entrez un troisième nombre : 5
# utiliser le théorème d'inégalité
# on peut dessiner un triangle :  True


# 2) cas où ce n'est pas OK
# Entrez un premier nombre : 5
# Entrez un second nombre : 8
# Entrez un troisième nombre : 3
# utiliser le théorème d'inégalité
# on ne peut pas dessiner un triangle :  False



if a+b>c and b+c>a and a+c>b:
 print("on peut dessiner un triangle : ", bool)
else :
 print("on ne peut pas dessiner un triangle : ", not bool)