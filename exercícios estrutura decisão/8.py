# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

valor_produto_1 = float(input('Digite o valor do primeiro produto: '))
valor_produto_2 = float(input('Digite o valor do segundo produto: '))
valor_produto_3 = float(input('Digite o valor do terceiro produto: '))

produto_mais_barato = 'primeiro'
menor_valor = valor_produto_1

if valor_produto_2 < valor_produto_1 and valor_produto_2 < valor_produto_3:
    menor_valor = valor_produto_2
    produto_mais_barato = 'segundo'
if valor_produto_3 < valor_produto_1 and valor_produto_3 < valor_produto_2:
    menor_valor = valor_produto_3
    produto_mais_barato = 'terceiro'

if valor_produto_1 == valor_produto_2 and valor_produto_2 == valor_produto_3:
    print('São os mesmos preços, pode escolher qual irá levar.')
else:
    print(f'Compre o {produto_mais_barato} produto, seu preço é R$ {menor_valor:,.2f}')