'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% 
Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
'''

valor_hora = float(input('Digite o valor da hora: '))
horas_trabalhadas = int(input('Digite quantas horas foram trabalhadas: '))

salario_bruto = valor_hora * horas_trabalhadas
porcentagem_imposto_renda = 0
desconto_imposto_renda = 0
desconto_inss = salario_bruto * 0.1
valor_fgts = salario_bruto * 0.11
total_descontos = desconto_inss
salario_liquido = 0

if salario_bruto > 0:
    if salario_bruto <= 900.00:
        porcentagem_imposto_renda = 0.0
    elif salario_bruto > 900.00 and salario_bruto <= 1500.00:
        porcentagem_imposto_renda = 0.05
    elif salario_bruto > 1500.00 and salario_bruto <= 2500.00:
        porcentagem_imposto_renda = 0.1
    else:
        porcentagem_imposto_renda = 0.2
else:
    print('Alguma informação está errada.')

desconto_imposto_renda = salario_bruto * porcentagem_imposto_renda
total_descontos += desconto_imposto_renda
salario_liquido = salario_bruto - total_descontos

print(f'Salário Bruto : ({horas_trabalhadas} * {valor_hora:,.2f}) : R$ {salario_bruto:,.2f}')
print(f'(-) IR ({porcentagem_imposto_renda * 100}%) : R$ {desconto_imposto_renda:,.2f}')
print(f'(-) INSS (10%): R$ {desconto_inss:,.2f}')
print(f'FGTS (11%) : R$ {valor_fgts:,.2f}')
print(f'Total de Descontos : R$ {total_descontos:,.2f}')
print(f'Salário Líquido : R$ {salario_liquido:,.2f}')