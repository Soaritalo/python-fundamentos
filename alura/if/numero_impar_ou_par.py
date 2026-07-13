#Escreva um programa que peça um número inteiro à pessoa usuária e determine se ele é par ou ímpar. Dica: Você pode utilizar o operador módulo %.
numero = int(input("digite um numero inteiro: "))
resultado = numero % 2 
if resultado == 1:
   print('numero impar !')
else: print('numero par! ')
input('aperte enter para sair')
