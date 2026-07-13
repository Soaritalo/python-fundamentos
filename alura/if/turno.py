# Escreva um programa que pergunte em qual turno a pessoa usuária estuda ("manhã", "tarde" ou "noite") e exiba a mensagem "Bom Dia!", "Boa Tarde!", "Boa Noite!", ou "Valor Inválido!", conforme o caso.
turno = input( 'qual turno voçê estuda?("manhã", "tarde" ou "noite"):  ').strip().lower()
if turno == "noite" :
    print('Boa noite magnata ')
elif turno == "manhã" or turno == "manha" or turno == MANHA:
    print('BOM DIA!!!!')
elif turno == "tarde":
    print('Herdeiro...') 
else:
    print('valor invalido tente novamente! ')
    input('pressione enter para sair')

input('pressione enter para sair')
