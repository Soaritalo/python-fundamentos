palavra_secreta = 'bobo'
letras_certas = ''
contador = 0
censura = ''
while censura != palavra_secreta:

    letra = input("Digite uma Letra: ")

    tamanho_letra = len(letra)

    censura = ''

    if tamanho_letra > 1:

        print('erro: mais de uma letra')
        continue
    for tentativa in letra:

        contador += 1
        if letra in palavra_secreta:
            letras_certas += letra

        censura = ''
    for i in palavra_secreta:
        if i in letras_certas:
            censura += i
        else:
            censura += '*'

    print(censura)

print("Você acertou! Foram", contador, "tentativas.")


