# Racines de polynôme
import math


a = float(input("Entrez un premier nombre a : "))
b = float(input("Entrez un second nombre b : "))
c = float(input("Entrez un troisième nombre c : "))

# print(a)
# print(b)
# print(c)
# type(a)
# type(b)
# type(c)

# delta_carré=b^2-4ac > 0
# a(x + (b+sqrt(delta))/2a)(x + (b-sqrt(delta))/2a)
# x1=-(b+sqrt(delta))/2a
# x2=-(b-sqrt(delta))/2a

# delta_carré=b^2-4ac = 0
# a(x + (b+sqrt(delta))/2a)(x + (b-sqrt(delta))/2a)
# x1=x2=-b/2a


# Calcul de Delta = Racine carrée de (b^2 - 4*a*c)
delta_carré = math.pow(b,2) - 4*a*c
print("delta_carré = ", delta_carré)

# si a=1, b=2, c=3 alors delta_carré<0
# si a=1, b=2, c=1 alors delta_carré=0 => delta = 0 => x1=x2=-b/2a=-1
# si a=1.5, b=8, c=2.5 alors delta_carré=49>0

if a==0.0:
 y = -(c/b)
 print("a est nul, et y = ", y)
elif delta_carré <0 :
 print("Pas de racine réelle")
elif delta_carré ==0 :
 x1=-b/(2*a)
 x2=-b/(2*a)
 print("Une racine double : ", x1)
 print("Une racine double : ", x2)
else :
 x1=-(b+math.sqrt(delta_carré))/(2*a)
 x2=-(b-math.sqrt(delta_carré))/(2*a)
 print("Deux racines réelles")
 print("Une racine : ", x1)
 print("L'autre racine : ", x2)