'''
Faça um programa que leia 5 números e informe a soma e a média dos números.
'''
soma = 0
for numero in range(5):
    numero = int(input('Digite um número: '))
    soma += numero
    
print(f'A soma dos números é {soma}')
print(f'A media dos números é {soma/5:.1f}')