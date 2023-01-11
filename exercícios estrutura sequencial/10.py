''' 
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a) o produto do dobro do primeiro com metade do segundo .
b) a soma do triplo do primeiro com o terceiro.
c) o terceiro elevado ao cubo.

'''

primeiro = int(input('Digite um número inteiro: '))
segundo = int(input('Digite outro número inteiro: '))
terceiro = float(input('Digite um número de ponto flutuante: '))

# o produto do dobro do primeiro com metade do segundo .

resposta_a = (primeiro * primeiro) * (segundo / 2)
print(f'A resposta da letra A é: {resposta_a:.2f}')

# a soma do triplo do primeiro com o terceiro.

resposta_b = (primeiro * 3) + terceiro
print(f'A resposta da letra B é: {resposta_b:.2f}')

# o terceiro elevado ao cubo.

resposta_c = terceiro * terceiro * terceiro
print(f'A resposta da letra C é: {resposta_c:.2f}')
