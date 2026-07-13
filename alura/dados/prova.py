NOTA = 0
Gabarito = ['D', 'A', 'C', 'B', 'A', 'D', 'C', 'C', 'A', 'B']
for questao in range (len(Gabarito)):
    resposta = input('Digite a sua reposta: ')
    resposta = resposta.upper()
    if resposta == Gabarito[questao]:
        NOTA +=1
print(f'Sua nota da prova foi:{NOTA}')
input('APERTE ENTER PARA SAIR')     

