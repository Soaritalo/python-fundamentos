# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def multiplicacao(*args):
    total = 1
    for numero in args:
        total = numero * total
        if numero == 0:
            print(f"{numero} seu numero é 0")
        elif numero % 2 == 0:
            print(f"{numero} seu numero é par")
        else :
            print(f"{numero} seu numero é impar")
    return total

numeros_digitados = input("Digite um numero para a multiplicação: ")
partes = numeros_digitados.split()
formato =  [int(_) for _ in partes]
resultadototal = multiplicacao(*formato)
print(resultadototal)

def par_Impar(numero):
    if resultadototal == 0:
        return("Seu numero deu 0")
    elif resultadototal % 2 == 0:
        return("seu numero é par")
    else : return("seu numero é impar")
print(par_Impar(resultadototal))


