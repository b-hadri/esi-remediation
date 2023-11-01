def imc(poids_en_kg, taille_en_m):
    return poids_en_kg / (taille_en_m ** 2)


poids_en_kg = int(input("Entrez le poids en kg : "))
taille_en_m = float(input("Entrez la taille en m : "))

print("IMC : ", imc(poids_en_kg, taille_en_m))
