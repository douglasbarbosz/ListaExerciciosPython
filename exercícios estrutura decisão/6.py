# Faça um Programa que leia três números e mostre o maior deles.

numero_1 = float(input('Digite o primeiro número: '))
numero_2 = float(input('Digite o segundo número: '))
numero_3 = float(input('Digite o terceiro número: '))

maior = 0

if numero_1 > numero_2 and numero_1 > numero_3:
    maior = numero_1
elif numero_2 > numero_1 and numero_2 > numero_3:
    maior = numero_2
else:
    maior = numero_3

if numero_1 == numero_2 and numero_2 == numero_3:
    print('São os mesmos números.')
else:
    print(f'{maior} é o maior número.')