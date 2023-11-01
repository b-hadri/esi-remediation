# perimetre_cercle
# *** Les fonctions en Python ***

# Une fonction calculant le périmètre d'un cercle de rayon donné:
def perimetre_cercle(rayon):
 return 2*3.14*rayon


r = float(input("Entrez la longueur (en cm) du rayon du cercle: "))

perimetre = perimetre_cercle(r)

print("Le périmètre du cercle de rayon",r,"vaut",perimetre,"centimètres")