'''
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.
'''
numero_1 = 1
numero_2 = 0

while numero_2 < 500:
    print(numero_1 + numero_2)
    aux = numero_1 + numero_2
    numero_1 = numero_2
    numero_2 = aux