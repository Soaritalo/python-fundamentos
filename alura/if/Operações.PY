# Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária qual operação ele deseja realizar. O resultado da operação deve incluir informações sobre o número - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.
n1 = float(input('Digite o primeiro numero: '))
n2 =  float(input('Digite o segundo numero: '))
escolha = input('Qual das operaçoes voce deseja realizar:  1--> impar ou par 2--> positivo ou negativo  3--> inteiro ou decimal ')
if escolha == "1":
    resultado1 = n1 % 2 
    resultado2 = n2 % 2
    if resultado1 == 1:
        print('numero impar !')
    else:
        print('numero par')
    if resultado2 == 1:
        print('numero impar !')
    else:
        print('numero par')
    input('aperte enter para sair')

elif escolha == "2":
    if n1 < 0 :
        print('numero negativo')
    elif n1 > 0 :
        print('numero é positivo')
    else:
        print('numero nulo')
    if n2 < 0:
        print('numero negativo')
    elif n2 > 0 :
        print('numero é positivo')
    else:
        print('numero nulo')
    input('aperte enter para sair')
else:
    resultado1 = n1 % 1
    resultado2 = n2 % 1
    print(f'resultado do numero dividido por 1: {resultado1}')
    print(f'resultado do numero dividido por 1: {resultado2}')
    if resultado1 == int(n1):
            print('numero inteiro!!! ')
    else: print('numero decimal ! ')
    if resultado2 == int(n2):
        print('numero inteiro!!! ')
    else: print('numero decimal ! ')

    input('aperte enter para sair')



