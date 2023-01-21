'''
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''
nome = input('Nome: ')
while len(nome) <= 3: 
    nome = input('Nome: ')

idade = int(input('Idade: '))
while idade < 0 or idade > 150:
    idade = int(input('Idade: '))

salario = float(input('Informe seu salário: '))
while salario < 0.0:
    salario = float(input('Informe seu salário: '))

sexo = input('Sexo: [f]eminino  [m]asculino: ').lower()
while sexo != 'f' and sexo != 'm':
    sexo = input('Sexo: [f]eminino  [m]asculino').lower()

estado_civil = input('Estado Civil: [s]olteira(o)  [c]asada(o)  [v]iúva(o)  [d]ivorciada(o): ')
while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
    estado_civil = input('Estado Civil: [s]olteira(o)  [c]asada(o)  [v]iúva(o)  [d]ivorciada(o): ')