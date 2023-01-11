# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
import math

valor_hora = float(input('Digite o valor da sua hora de trabalho: '))
horas_trabalhadas = float(input('Digite quantas hotas você trabalhou nesse mês: '))

salario = valor_hora * horas_trabalhadas

print(f'O seu salário nesse mês é de R$ {salario:,.2f}')