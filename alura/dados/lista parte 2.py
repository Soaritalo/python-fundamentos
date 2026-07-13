#Faça um código que colete em uma lista 5 números inteiros quaisquer e imprima a lista. Exemplo: [1,4,7,2,4].
lista = []
numeros = 0
while numeros < 5:
   numeral = int(input('Digite um numero inteiro: '))
   lista.append(numeral)
   numeros += 1
print(f'Os numeros digitados foram: {lista}')
input('Aperte enter para sair')
