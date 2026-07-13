nota1 = int(input('Me fale a nota da primeira prova: '))
nota2 = int(input('Me fale a nota da segunda prova: '))
nota3 = int(input('Me fale a nota da terceira  prova: '))
media = float(nota1 + nota2 + nota3) / 3
print(media)
if media < 6:
    print('Voce se deu mal... Reprovado!')
else :print('Mandou bem magnata! Aprovado!!')
