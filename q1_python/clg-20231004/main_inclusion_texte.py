import inclusion_texte

texte1 = input('Entrez un texte : ')
texte2 = input('Entrez un autre texte : ')


if (inclusion_texte.est_inclus(texte1, texte2)):
 print('Un des deux textes EST inclus dans l\'autre')
else:
 print('Aucun des textes n\'est inclus dans l\'autre')
