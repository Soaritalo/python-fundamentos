#Escreva um programa que peça um número à pessoa usuária e informe se ele é inteiro ou decimal.
numero = float(input("digite um numero: "))
resultado = numero % 1
print(f'resultado do numero dividido por 1: {resultado}')
if resultado == 0:
   print('numero inteiro!!! ')
else: print('numero decimal ! ')
input('aperte enter para sair')
