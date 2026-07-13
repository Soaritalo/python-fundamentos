# Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “a” trocadas pela caractere “@”.
# na tabela unicode o caractere @ é o numero 64
frase = input('Digite uma frase: ')
print(frase.lower().replace('a',chr(64)))


# Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as consoantes “s” trocadas pelo caractere “$”.
# na tabela unicode o caractere $ é o numero 36 
frase2 = input(' Digite uma frase pra ver uma magica ')
print(frase2.lower().replace('s',chr(36)))
