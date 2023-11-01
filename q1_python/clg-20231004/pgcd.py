# Un programme PGCD

import math

print(" **** Bienvenue ! **** ")
x = int(input(" Entrez un nombre : "))
y = int(input(" Entrez un nombre : "))
le_PGCD = math.gcd(x, y)
print("Le PGCD de ",x, y, " vaut : ", le_PGCD)