'''
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.
'''
valor = int(input('Digite quantos números da série Fibonacci deseja ver: '))
numero_1 = 1
numero_2 = 0

for i in range(valor):
    print(numero_1 + numero_2)
    aux = numero_1 + numero_2
    numero_1 = numero_2
    numero_2 = aux