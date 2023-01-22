'''
Faça um programa que leia 5 números e informe o maior número.
'''
maior_numero = 0

for numero in range(5):
    numero = int(input('Digite um número: '))
    
    if numero > maior_numero:
        maior_numero = numero
        
print(f'O maior número é {maior_numero}')