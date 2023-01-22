'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
'''

altura = float(input('Digite sua altura: '))
sexo = input('Digite seu sexo: [M]asculino [F]eminino: ').lower()
peso_ideal = 0

if sexo == 'm':
  peso_ideal = (72.7 * altura) - 58
elif sexo == 'f':
  peso_ideal = (62.1 * altura) - 44.7
else:
  print('Não pode chegar aqui.')
  
print(f'Seu peso ideal seria: {peso_ideal:.2f}')