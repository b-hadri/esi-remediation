import random
# les_valeurs = [2,3,4,5,6,7,8,9,10,'valet','dame','roi','as']
# les_couleurs = ['pique','trèfle','cœur','carreau' ]

# Retourne un nombre aléatoire entre a et b (appelée par la fonction lettres())
def hasard (a,b):
 return random.randint(a,b)

# Tire une couleur aléatoire et la retourne
def tirer_carte ():
 les_valeurs = [2,3,4,5,6,7,8,9,10,'valet','dame','roi','as']
 les_couleurs = ['pique','trèfle','cœur','carreau' ]
 nb_valeurs = len(les_valeurs)
 nb_couleurs = len(les_couleurs)

 valeur = les_valeurs[hasard(0,nb_valeurs-1)]
 couleur = les_couleurs[hasard(0, nb_couleurs-1)]

 return [valeur, couleur]
