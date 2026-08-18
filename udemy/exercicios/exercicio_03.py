#   Enunciado:Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
    #menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
    #"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".


def main():
    primeiro_norme = input("Digite seu primeiro nome: ")
    tamanho = len(primeiro_norme)
    if tamanho <= 4:
            print("seu nome é pequeno!")
    elif   5 <= tamanho <= 6 :
            print("seu nome é normal!")
    else: 
           print("SEU NOME É GRANDE")
main()