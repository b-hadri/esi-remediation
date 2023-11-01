#adresse_valide(adresse)
#elle contient UNE FOIS le symbole arobase ’@’,
#elle contient au moins un point ’.’,
#le premier caractère et le dernier caractère ne sont ni ’@’ ni ’.

import adresse_valide

adresse = input("Entrez une adresse : ")

adresse_valide.adresse_valide(adresse)
print(adresse)
print(adresse_valide.adresse_valide(adresse))

if adresse_valide.adresse_valide(adresse):
   print("adresse correcte") 
else:
   print("adresse incorrecte") 
