##        """ Calculadora com While """
# numero1 = float(input("Digite o primeiro numero: "))
# numero2 = float(input("Digite o segundo numero: "))

while True:
    numero1 = float(input("Digite o primeiro numero: "))
    numero2 = float(input("Digite o segundo numero: "))
    menu = input('Digite o operador (+-/*): ')
    if menu == '+':
        Soma = numero1 + numero2
        print(Soma)
        continue
    elif menu == '-':
        subtracao = numero1 - numero2
        print(subtracao)
        continue
    elif menu == '/':
        divisao =     numero1 / numero2
        print(divisao)
        continue
    elif menu == '*':
        multiplicacao = numero1 * numero2
        print(multiplicacao)
        continue
    else:
        print('digite um numero/operador valido!')
    sair = input('Você quer sair? [s/n]: ').lower().startswith('s')
    if sair == True:
        break
    else: 
        continue