# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor = int(input('Digite um número qualquer: '))

if valor > 0:
    print(f'{valor} é positivo')
elif valor < 0:
    print(f'{valor} é negativo')
else: 
    print('Seu número é 0')