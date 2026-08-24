# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
tentativas = 0
acertos = 0
erros = 0 
for item in perguntas:
    p1 = item.get('Pergunta')
    print(p1)
    o1 = item.get('Opções')
    tentativa = input('Digite a resposta: ')
    r1 = item.get('Resposta')
    if tentativa == r1:
        print('Você acertou!!!!!!!!!!!')
        acertos += 1
    else: 
        print('Voce errou :( ')
        erros += 1
print(f'Foram {acertos} acertos e {erros} erros')
    