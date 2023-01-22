'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
'''
numero = int(input('Informe um número: '))
conta_completa = f'{numero}!={numero} '
resultado = numero
numero_subtraido = numero - 1

for i in range(numero - 1):
    resultado = resultado * numero_subtraido

    if numero_subtraido == 1:
        conta_completa += f'{numero_subtraido}'
    else:
        conta_completa += f'{numero_subtraido} '

    numero_subtraido -= 1

conta_completa += f'={resultado}'
conta_completa = conta_completa.replace(' ', '.')
print(conta_completa)