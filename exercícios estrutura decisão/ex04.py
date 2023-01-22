# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Digite uma letra qualquer: ').lower()

tamanho = len(letra)
vogais = 'aeiou'
consoantes = 'bcdfghjklmnpqrstvwxyz'

if tamanho == 1:
    if letra in vogais:
        print(f'{letra.upper()} é vogal.')
    elif letra in consoantes:
        print(f'{letra.upper()} é consoante.')
    else:
        print('Não é letra')
else:
    print('Mais de um caracter foi digitado')
