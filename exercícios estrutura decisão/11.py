'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% 
Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
'''

salario = float(input('Digite o salário do funcionário: '))
porcentagem_aumento = 0
valor_aumento = 0
novo_salario = 0

if salario > 0:
    if salario <= 280.00:
        porcentagem_aumento = 0.2
        valor_aumento = salario * porcentagem_aumento
        novo_salario = salario + valor_aumento
    elif salario > 280.00 and salario < 1500.00:
        porcentagem_aumento = 0.15
        valor_aumento = salario * porcentagem_aumento
        novo_salario = salario + valor_aumento
    else:
        porcentagem_aumento = 0.1
        valor_aumento = salario * porcentagem_aumento
        novo_salario = salario + valor_aumento

    print(f'O salário antes do reajuste: R$ {salario:,.2f}')
    print(f'O percentual de aumento foi de {porcentagem_aumento * 100}%')
    print(f'O valor do aumento foi de R$ {valor_aumento:,.2f}')
    print(f'O novo salário, após o aumento é de R$ {novo_salario:,.2f}')
else:
    print('Digite um salário real.')