'''
Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
'''
numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))

while numero_1 > numero_2:
    numero_1 = int(input('Digite um número: '))
    numero_2 = int(input('Digite outro número: '))
else:
    for numero in range(numero_1 + 1, numero_2):
        print(numero)