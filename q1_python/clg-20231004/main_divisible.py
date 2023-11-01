import divisible

a = int(input('Entrez un nombre entier : '))
b = int(input('Entrez un autre nombre entier : '))


if (divisible.est_divisible(a, b)):
 print('Un des deux nombres EST divisible par l\'autre')
else:
 print('Un des deux nombres n\'est PAS divisible par l\'autre')
