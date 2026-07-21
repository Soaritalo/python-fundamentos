lista = []
lista_numerada = enumerate(lista)
while True:
    menu = input('  Selecione uma opção: \n[i]inserir [a]pagar [l]istar ').strip().lower()
    if menu == 'i':

        print("adicionar item ")
        item_adicionar = input("digite o item a ser adicionado: ").strip().lower()
        lista.append(item_adicionar)
        continue

    elif menu == "a":
        print(" Remover item selecionado")
        item_remover = input("digite o item que deseja remover: ").lower().strip()
        try:
            del lista[item_remover]
        except ValueError:
            print('Náo foi possivel apagar esse indice')
        except IndexError:
            print('Digite o nome do item a remover')
        except:
            print('nao existe na lista')

        continue

    elif menu == "l":
        if len(lista) == 0:
            print(' Nada a listar!!! ')
            continue

        else:
            for item in enumerate(lista):
                indice,nome = item
                print(indice, nome)
            continue

        