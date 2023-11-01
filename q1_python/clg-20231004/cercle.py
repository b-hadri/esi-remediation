# Dans ou hors du cercle
import math

bool = True;

x = int(input("Entrez la coordonnée x : "))
y = int(input("Entrez la coordonnée y : "))
xc = int(input("Entrez le centre xc : "))
yc = int(input("Entrez le centre yc : "))
r = int(input("Entrez le rayon : "))

# équation du cercle => périmètre du cercle : (x-xc)^2 + (y-yc)^2 = r^2 
# Tous les points vérifiant l'équation du cercle sont sur le cercle
#(x-xc)^2 + (y-yc)^2 = r^2 
# Si on est au centre (xc, yc): (xc-xc)^2 + (yc-yc)^2 = 0 < r^2
# Calcul de (x-xc)^2 + (y-yc)^2

# Cas 1)
# Entrez la coordonnée x : 1
# Entrez la coordonnée y : 5
# Entrez le centre xc : 1
# Entrez le centre yc : 2
# Entrez le rayon : 4
# Le point est dans le cercle :  True

# Cas 2)
# Entrez la coordonnée x : 2
# Entrez la coordonnée y : 6
# Entrez le centre xc : 1
# Entrez le centre yc : 2
# Entrez le rayon : 4
# Le point n'est pas dans le cercle :  False

# Cas 3)
# Entrez la coordonnée x : 5
# Entrez la coordonnée y : 2
# Entrez le centre xc : 1
# Entrez le centre yc : 2
# Entrez le rayon : 4
# Le point est sur le cercle



res = math.pow((x-xc), 2) + math.pow((y-yc), 2)

if res < math.pow(r, 2):
 print("Le point est dans le cercle : ", bool)
elif res > math.pow(r, 2):
 print("Le point n'est pas dans le cercle : ", not bool)
else :
 print("Le point est sur le cercle")
