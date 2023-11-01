# Un programme intérêts
# 1*montant + 2%*montant = montant*(1+2%)=montant*(1+0.02)=montant*1.02

print(" **** Bienvenue ! **** ")
m = float(input(" Entrez le montant : "))
années = int(input("Entrez le nombre d'années : "))
somme_interet = 0
for i in range(années):
    interet_années = m*0.02
    somme_interet = somme_interet + interet_années
    m=m+interet_années

print("le montant avec intérêts sur toutes les années est : ", somme_interet)

#100
#1) 100*0.02 = 2
#2) 102*0.02 = 2,04
#3) 104,04*0.02 = 2,0808
#4) (104,04+ 2,0808)*0,02=2,122416
#2+2,04+2,0808+2,122416=8,243216
