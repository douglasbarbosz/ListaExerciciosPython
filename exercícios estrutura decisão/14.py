'''
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
  
  O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
'''
nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))

media = (nota_1 + nota_2) / 2
conceito = ''
aprovado = 'ABC'

if media <= 10.0 and media >= 0:
    if media >= 9.0 and media <= 10.0:
        conceito = 'A'
    elif media >= 7.5 and media < 9.0:
        conceito = 'B'
    elif media >= 6.0 and media < 7.5:
        conceito = 'C'
    elif media >= 4.0 and media < 6.0:
        conceito = 'D'
    else:
        conceito = 'E'

    print(f'Nota 1: {nota_1:.1f}')
    print(f'Nota 2: {nota_2:.1f}')
    print(f'Media: {media:.1f}')
    print(f'Conceito: {conceito}')
    
    if conceito in aprovado:
        print('APROVADO!')
    else:
        print('REPROVADO!')
else:
    print('Nota inválida!')