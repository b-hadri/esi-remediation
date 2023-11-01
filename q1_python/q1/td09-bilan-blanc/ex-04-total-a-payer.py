
somme = 0
prix = 0
quantité = 0

while prix != -1:
    somme += quantité * prix
    prix = float(input("Prix : "))
    if prix != -1:
        quantité = int(input("Quantité : "))

print(somme, " euros")

