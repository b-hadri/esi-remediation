import moyenne

a = int(input('Entrez un nombre : '))
b = int(input('Entrez un 2nd nombre : '))
c = int(input('Entrez un 3ème nombre : '))

print("La moyenne des 3 nombres est : ", moyenne.moyenne(a,b,c))
print("La moyenne des 3 nombres", a, " ", b, " ", c, " est : ",
moyenne.moyenne(a,b,c))

# $ python main_moyenne.py
# Entrez un nombre : 1
# Entrez un 2nd nombre : 10
# Entrez un 3ème nombre : 10
# La moyenne des 3 nombres est :  7.0
