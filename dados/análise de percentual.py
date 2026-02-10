lista = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]
lista_percentual =[]
tamanho = len(lista)
for i in range(1,len(lista)):
    amostra_passada = lista[i-1]
    amostra_atual = lista[i]
    percentual = 100 * (amostra_atual - amostra_passada) / (amostra_passada)
    lista_percentual.append(percentual)
print(f'Ao todo foram {tamanho} dias')
print("Os percentuais foram: ")
print(", ".join(f"{p:.2f}%" for p in lista_percentual))
print(f'Os valores originais: {lista}')
input('Aperte enter para sair ')
