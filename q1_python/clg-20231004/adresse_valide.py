#adresse_valide(adresse)
#elle contient UNE FOIS le symbole arobase ’@’,
#elle contient au moins un point ’.’,
#le premier caractère et le dernier caractère ne sont ni ’@’ ni ’.




def adresse_valide(adresse):
    bool = True
    if '.' in adresse and adresse.count('@')==1 and adresse[0]!='.' and adresse[len(adresse)-1]!='.' and adresse[0]!='@' and adresse[len(adresse)-1]!='@':
 #   print("adresse correcte")    
        return bool
    else:
#   print("Ceci n'est pas une adresse valide")
        return (not bool)
   
    