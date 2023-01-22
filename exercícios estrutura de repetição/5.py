'''
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
'''
populacao_pais_a = int(input('Digite a população do País A: '))
taxa_pais_a = float(input('Digite a porcentagem de crescimento anual do País A: '))
populacao_pais_b = int(input('Digite a população do País B: '))
taxa_pais_b = float(input('Digite a porcentagem de crescimento anual do País B: '))
anos = 0

while populacao_pais_a < populacao_pais_b:
    populacao_pais_a += populacao_pais_a * (taxa_pais_a / 100)
    populacao_pais_b += populacao_pais_b * (taxa_pais_b / 100)
    anos += 1

print(f'São necessários {anos} anos.')