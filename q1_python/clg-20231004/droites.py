# Droites

print("Droite ax+by+c=0")
a = int(input("Entrez a : "))
b = int(input("Entrez b : "))
c = int(input("Entrez c : "))
print("ax+by+c")


if a==0 and b==0:
 print("a et b ne peuvent pas être nuls sinon ce n'est plus une droite")
elif a==0 :
 y=-c/b
 print("droite parallèle à l'axe des x : pas d'intersection avec l'axe des x, y = ", y)
elif b==0 :
 x=-c/a
 print("droite parallèle à l'axe des y : pas d'intersection avec l'axe des y, x = ", x)
else:
 x=-c/a
 y=-c/b
 print("la droite ax+by+c est : ", a, "*x + ", b, "*y + ", c)
 print("les coordonnées des points d'intersection sont:")
 print("Intersection avec l'axe des x (y=0) :(", x, ", 0)")
 print("Intersection avec l'axe des y (x=0) :(", y, ", 0)")


# cas général ax+by+c = 0 => y = (-a/b)*x -c/b
# Intersection de l'équation avec l'axe des X (y=0)
# ax+b*0+c=0  => x=-c/a donc Intersection A(-c/a,0)
# Si la droite est // à l'axe des x, il n'y a pas d'intersection
# pas d'intersection si y = constante 


# Intersection de l'équation avec l'axe des Y (x=0)
# a*0+by+c=0  => y=-c/b donc Intersection B(0,-c/b)
# Si la droite est // à l'axe des y, il n'y a pas d'intersection
# pas d'intersection si x = constante

# Les coordonnées des deux points d'intersection sont :
# A(-c/a, 0) et B(0, -c/b)