# On importe le module désiré ...
import carre

x = float(input("Entrez la longueur (en cm) du côté du carré: "))

# ... et on fait appel aux fonctions nécessaires
if x<=0:
 print("le côté doit être >0!")
else:
 aire = carre.aire_carré(x)
 print("L'aire du carré de côté",x,"vaut",aire,"centimètres")