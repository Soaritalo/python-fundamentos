#Escreva um programa que leia três números e os exiba em ordem decrescente.
numero1 = float(input('digite o primeiro numero: '))
numero2 = float(input('digite o segundo numero: '))
numero3 = float(input('digite o terceiro numero : '))
if numero1 > numero2 and numero1 > numero3:
    maior = numero1
    if numero2 > numero3:
        meio = numero2
        menor = numero3
    else:
        meio = numero3
        menor = numero2

elif numero2 > numero1 and numero2 > numero3:
      maior = numero2
      if numero1 > numero3:
          meio = numero1
          menor = numero3
      else:
        meio = numero3
        menor = numero1

elif numero3 > numero2 and numero3 > numero1:
    maior = numero3
    if numero2 > numero1:
        meio = numero2
        menor = numero1
    else: 
        meio = numero1
        menor = numero2


print(f'segue os valores em ordem decrescente {maior} {meio} {menor}')
input('pressione enter para sair')

