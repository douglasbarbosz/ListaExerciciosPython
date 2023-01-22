'''
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.
'''
base = int(input('Digite a base para calcular: '))
expoente = int(input('Agora digite o expoente: '))
resultado = base

for i in range(expoente - 1):
    resultado = resultado * base
    
print(resultado)