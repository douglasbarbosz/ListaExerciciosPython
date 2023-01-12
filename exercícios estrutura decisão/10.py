# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

horario = input('Digite o turno que você estuda: [M]atutino / [V]espertino / [N]oturno: ').lower()

mensagem = ''

if horario == 'm':
    mensagem = 'Bom Dia!'
elif horario == 'v':
    mensagem = 'Boa Tarde!'
elif horario == 'n':
    mensagem = 'Boa Noite!'
else: 
    mensagem = 'Valor Inválido!'

print(mensagem)