# On importe le module désiré ...
import cercle_td5

r = float(input("Entrez la longueur (en cm) du rayon du cercle: "))

# ... et on fait appel aux fonctions nécessaires
perimetre = cercle_td5.perimetre_cercle(r)

print("Le périmètre du cercle de rayon",r,"vaut",perimetre,"centimètres")