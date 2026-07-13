#Escreva um programa que pergunte sobre o preço de três produtos e indique qual é o produto mais barato para comprar.
produto1 = float(input('digite o preço do primeiro produto: '))
produto2 = float(input('digite o preço do segundo produto: '))
produto3 = float(input('digite o preco do terceiro produto: '))

if produto1 < produto2 and produto1 < produto3:
    barato = produto1
    print('produto 1 é o mais barato')
elif produto2 < produto1 and produto2 < produto3:
    barato = produto2
    print('produto 2 é o mais barato')
elif produto3 < produto2 and produto3 < produto1:
    barato = produto3
    print('produto 3 é o mais barato')

print(f'o preço do produto mais barato é de {barato}R$ ')
input('enter para sair')
