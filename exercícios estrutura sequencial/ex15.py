'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''
tamanho_metros = float(input('Digite o tamanho em metros quadrados da área a ser pintada: '))

litros = round(tamanho_metros / 3 + 0.5)
latas = round(litros / 18 + 0.5)
preco_total = latas * 80.00

print(f'Serão necessárias {latas:.0f} latas que custarão R$ {preco_total:,.2f}')