# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

valor = input('Digite seu sexo: [F]eminino ou [M]asculino: ').lower()

if valor == 'f':
    print('F - Feminino')
elif valor == 'm':
    print('M - Masculino')
else:
    print('Sexo inválido.')
