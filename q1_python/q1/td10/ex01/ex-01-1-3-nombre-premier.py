

def est_nombre_premier(nombre):
    for i in range(2, nombre):
        if nombre % i == 0:
            return False
    return True



def main():
    while True:
        nombre = int(input("Entrez un nombre entier : "))
        if est_nombre_premier(nombre):
            print("C'est un nombre PREMIER")
        else:
            print("Non premier")
        print("")

main()