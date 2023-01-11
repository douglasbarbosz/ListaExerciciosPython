# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

temperatura_c = float(input('Digite a temperatura em graus Celsius para ser convertido: '))

temperatura_f = temperatura_c * 1.8 + 32

print(f'{temperatura_c:.1f} C = {temperatura_f:.1f} F')