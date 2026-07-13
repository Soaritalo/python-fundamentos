#Vamos entender a distribuição de idades de pensionistas de uma empresa de previdência. Escreva um programa que leia as idades de uma quantidade não informada de clientes e mostre a distribuição em intervalos de [0-25], [26-50], [51-75] e [76-100]. Encerre a entrada de dados com um número negativo.
idade0_25 = 0
idade26_50 = 0
idade51_75 = 0
idade76_100 = 0
total = 0
idades = int(input('Digite uma idade: '))
while idades >= 0:
    total+=1
    idades = int(input("Digite uma idade (número negativo para encerrar): "))
    if 0 <= idades <= 25:
        idade0_25+=1
    elif 26 <= idades <= 50:
        idade26_50+=1
    elif 51 <= idades <= 75:
        idade51_75+=1
    elif 76 <= idades <= 100:
        idade76_100+=1
    else:       
        print("Valor incorreto digitado")
print(f'pessoas de 0 a 25 anos: {idade0_25}')
print(f'pessoas de 26 a 50 anos: {idade26_50}')
print(f'pessoas de 51 a 75 anos: {idade51_75}')
print(f'pessoas de 76 a 100 anos: {idade76_100}')
print(f'total de idades digitadas: {total}')
input('Aperte enter para sair')
