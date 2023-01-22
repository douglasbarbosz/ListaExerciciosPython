# Faça um Programa que leia três números e mostre o maior e o menor deles.

numero_1 = float(input('Digite o primeiro número: '))
numero_2 = float(input('Digite o segundo número: '))
numero_3 = float(input('Digite o terceiro número: '))

maior = numero_1
menor = numero_1

# Estrutura para encontrar o maior valor
if numero_2 > numero_1 and numero_2 > numero_3:
    maior = numero_2

if numero_3 > numero_1 and numero_3 > numero_2:
    maior = numero_3

# Estrutura para encontrar o menor valor
if numero_2 < numero_1 and numero_2 < numero_3:
    menor = numero_2

if numero_3 < numero_1 and numero_3 < numero_2:
    menor = numero_3

if numero_1 == numero_2 and numero_2 == numero_3:
    print('São os mesmos números.')
else:
    print(f'{maior} é o maior valor e {menor} é o menor')