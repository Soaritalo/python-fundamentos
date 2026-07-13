#Faça um programa que, ao inserir um número qualquer, cria uma lista contendo todos os números primos entre 1 e o número digitado.
lista = []
numero = int(input("Digite um numero: "))

for n in range (2,numero+1):
        eh_primo = True
        for i in range(2, n):
            if n % i == 0:
                eh_primo = False
                break
        if eh_primo:
            lista.append(n)
print(lista)
input('aperte ENTER PARA SAIR')
