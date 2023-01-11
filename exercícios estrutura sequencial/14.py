''' 
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$

'''

valor_hora = float(input('Digite o valor da sua hora de trabalho: '))
horas_trabalhadas = float(input('Digite quantas hotas você trabalhou nesse mês: '))

salario_bruto = valor_hora * horas_trabalhadas

valor_imposto_renda = salario_bruto * 0.11
valor_inss = salario_bruto * 0.08
valor_sindicato = salario_bruto * 0.05
descontos = valor_imposto_renda + valor_inss + valor_sindicato
salario_liquido = salario_bruto - descontos

print(f'+ Salário Bruto : R$ {salario_bruto:,.2f}')
print(f'- IR (11%) : R$ {valor_imposto_renda:,.2f}')
print(f'- INSS (8%) : R$ {valor_inss:,.2f}')
print(f'- Sindicato (5%) : R$ {valor_sindicato:,.2f}')
print(f'= Salário Líquido : R$ {salario_liquido:,.2f}')