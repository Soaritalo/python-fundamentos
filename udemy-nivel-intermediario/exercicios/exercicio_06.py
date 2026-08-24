# Exercicios 
# Crie funcoes que ducplicam, triplicam e quadruplicam 
# o numero recebido como parametro.

def duplicar(numero):
    return numero * 2
def triplicar(numero):
    return numero * 3
def qudruplicar(numero):
    return numero * 4 


while True:
    menu_digitado = int(input("Digite um numero do menu | 2 -- duplicar | 3 -- triplicar | 4 -- quadruplica | 0 -- sair "))
    numero = int(input("Digite um numero: "))
    if menu_digitado == 2:
        print(duplicar(numero))
    elif menu_digitado == 3 :
        print(triplicar(numero))
    elif menu_digitado == 4:
        print(qudruplicar(numero))
    elif menu_digitado == 0:
        break
    else :
        print("Digite um numero/menu valido!!!!!!!!!!!!!!!!!!!!!!!!")
        continue