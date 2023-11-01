# Mon 5ème script Python !
#
# Un programme calculant le temps en secondes sur base d'un temps donné en heures, minutes et secondes
# heures, minutes, secondes sont entrés au clavier par l'utilisateur

print(" **** Bienvenue ! **** ")
heures = int(input("Entrez les heures : "))
minutes = int(input("Entrez les minutes : "))
secondes = int(input("Entrez les secondes : "))
temps_en_secondes = heures*3600 + minutes*60 + secondes
print("Le temps en secondes vaut:", temps_en_secondes)