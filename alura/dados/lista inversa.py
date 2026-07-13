#Colete novamente 5 inteiros e imprima a lista em ordem inversa à enviada.
lista = []
numeros = 0
while numeros < 5:
   numeral = int(input('Digite um numero inteiro: '))
   lista.append(numeral)
   numeros += 1
lista.reverse()
print(f'Os numeros digitados foram: {lista}')
input('Aperte enter para sair')
