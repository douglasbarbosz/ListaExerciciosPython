'''
Altere o programa anterior para mostrar no final a soma dos números.
'''
numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))
soma = 0

while numero_1 > numero_2:
    numero_1 = int(input('Digite um número: '))
    numero_2 = int(input('Digite outro número: '))
else:
    for numero in range(numero_1 + 1, numero_2):
        soma += numero
        print(numero)
    
print(f'A soma dos números no intervalo é {soma}')