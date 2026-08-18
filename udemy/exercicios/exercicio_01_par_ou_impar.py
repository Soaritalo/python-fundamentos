#faça um programa que peça ao ussuario para digitar um número inteiro e, em seguida, exiba se o número é par ou ímpar.caso o usuario nao digite um número inteiro, o programa deve exibir uma mensagem de erro e solicitar que o usuário digite novamente até que um número inteiro válido seja fornecido.





def main():
    numero = input('Digite um número inteiro: ')
    if numero.isdigit():
        verificar = int(numero) % 2
        if verificar == 0:
            print('O número é par.')
        else:
            print('O número é ímpar.')
    else:
        print('Digite um numero valido')
        return main()
main()