'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''
nome_usuario = input('Usuário: ')
senha = input('Senha: ')

while nome_usuario == senha:
    print('Erro! O usuário e a senha não podem ser iguais.')
    nome_usuario = input('Usuário: ')
    senha = input('Senha: ')
else:
    print('Cadastrado!')