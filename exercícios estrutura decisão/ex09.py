# Faça um Programa que leia três números e mostre-os em ordem decrescente.

numero_1 = float(input('Digite o primeiro número: '))
numero_2 = float(input('Digite o segundo número: '))
numero_3 = float(input('Digite o terceiro número: '))


if numero_1 > numero_2:
    if numero_2 > numero_3:
        print(f'{numero_1:.1f}, {numero_2:.1f}, {numero_3:.1f}')
    elif numero_1 > numero_3:
        print(f'{numero_1:.1f}, {numero_3:.1f}, {numero_2:.1f}')
    else:
        print(f'{numero_3:.1f}, {numero_1:.1f}, {numero_2:.1f}')
else:
    if numero_2 > numero_3:
        if numero_1 > numero_3:
            print(f'{numero_2:.1f}, {numero_1:.1f}, {numero_3:.1f}')
        else: 
            print(f'{numero_2:.1f}, {numero_3:.1f}, {numero_1:.1f}')
    else: 
        print(f'{numero_3:.1f}, {numero_2:.1f}, {numero_1:.1f}')