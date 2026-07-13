input(' A seguir voce digitara os lados do triangulo. Aperte enter para continuar...')
l1 = float(input(' Primeiro lado do triangulo: '))
l2 = float(input('Segundo lado do triangulo: '))
l3 = float(input('Terceiro lado do triangulo: '))
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
