#Escreva um programa que peça à pessoa usuária três números que representam os lados de um triângulo. O programa deve informar se os valores podem ser utilizados para formar um triângulo e, caso afirmativo, se ele é equilátero, isósceles ou escaleno. Tenha em mente algumas dicas:Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes.
input(' A seguir voce digitara os lados do triangulo. Aperte enter para continuar...')
l1 = float(input(' Primeiro lado do triangulo: '))
l2 = float(input('Pegundo lado do triangulo: '))
l3 = float(input('Perceiro lado do triangulo: '))
if l1 <= 0 or l2 <= 0 or l3 <= 0:
    print('Ai nao né chefe numero abaixo ou igual a 0 nao da ')
    input('Aperte enter para sair ')
    exit()
if l1 == l2 and l3 == l2 and l1==l3:
    print(' Seu triangulo é equilatero! ')
elif l2 == l3 and l2 > l1 or l2 == l1 and l2 > l3 or l2 == l1 and l2 < l3 or l2 == l3 and l2 < l1:
    print(' Seu triangulo é isósceles ')
else:
    print('seu triangulo é escaleno')
input(' Aperte enter para continuar ')
