# Un programme hasard

import random

print(" **** Bienvenue ! **** ")
m = int(input(" Entrez un nombre : "))
n = int(input(" Entrez un nombre : "))
aléatoire = random.randint(m, n)
print("le nombre au hasard compris entre ",m, " et ", n, " vaut : ", aléatoire)