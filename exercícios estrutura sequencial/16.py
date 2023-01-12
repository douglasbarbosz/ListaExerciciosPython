''' 
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

'''

tamanho_metros = float(input('Digite o tamanho em metros quadrados da área a ser pintada: '))

litros = round(tamanho_metros / 6 + 0.5)
latas = round(litros / 18 + 0.5)
galoes = round(litros / 3.6 + 0.5)
preco_total_latas = latas * 80.00
preco_total_galoes = galoes * 25.00

# comprar apenas latas de 18 litros

print(f'Serão necessárias {latas:.0f} latas que custarão R$ {preco_total_latas:,.2f}')

# comprar apenas galões de 3,6 litros;

print(f'Serão necessárias {galoes:.0f} latas que custarão R$ {preco_total_galoes:,.2f}')

# misturar latas e galões, de forma que o desperdício de tinta seja menor. 
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

# NÃO TERMINADO