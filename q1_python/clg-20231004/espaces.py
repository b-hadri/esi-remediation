# Un programme espaces

phrase = input("Entrez une phrase: ")
nb_espaces = phrase.count(' ')
print(nb_espaces)

if nb_espaces==0:
 print("il n'y a pas d'espace")
elif nb_espaces ==1 :
 print("il y a un seul espace")
else:
 print("il y a plus d'un espace")