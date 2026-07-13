#Escreva um programa que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. Como exemplo, para o número 2, a tabuada deve ser mostrada no seguinte formato:
#Tabuada do 2:
#2 x 1 = 2
#2 x 2 = 4
#[...]
#2 x 10 = 20
N1 = int(input('Digite um numero inteiro: '))
for numeros in range (1,11):
    resultado = numeros * N1
    print(f'{N1} x {numeros} = {resultado}')
input('aperte enter para sair')
