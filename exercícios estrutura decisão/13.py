# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

valor = input('Digite um número e direi qual o dia da semana correspondente: ')

valores_aceitos = '1234567'
dia = ''

if valor in valores_aceitos:
    if valor == '1':
        dia = 'Domingo'
    elif valor == '2':
        dia = 'Segunda-feira'
    elif valor == '3':
        dia = 'Terça-feira'
    elif valor == '4':
        dia = 'Quarta-feira'
    elif valor == '5':
        dia = 'Quinta-feira'
    elif valor == '6':
        dia = 'Sexta-feira'
    else: 
        dia = 'Sábado'
    
    print(f'{valor} - {dia}')
    
else: 
    print('Valor Inválido!')