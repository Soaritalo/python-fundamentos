#qual letra apareceu mais vezes na frase? (iterando strings com while)

frase = input("Digite uma frase: ")

contagem = {}
i = 0
while i < len(frase):
    letra = frase[i]
    contagem[letra] = contagem.get(letra, 0) + 1
    i += 1

campea = max(contagem, key=contagem.get)
print(f"Letra mais frequente: '{campea}' ({contagem[campea]}x)")