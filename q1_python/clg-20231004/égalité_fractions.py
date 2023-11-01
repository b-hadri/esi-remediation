# Égalité de fractions

bool = True;
a = int(input("Entrez un premier nombre : "))
b = int(input("Entrez un second nombre : "))
c = int(input("Entrez un troisième nombre : "))
d = int(input("Entrez un quatrième nombre : "))

if b==0 or d==0:
 print("b ou d ne peuvent être nuls")
elif a/b == c/d :
 print(bool)
else :
 print(not bool)