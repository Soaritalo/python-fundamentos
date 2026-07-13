#Em uma eleição para gerência em uma empresa com 20 pessoas colaboradoras, existem quatro candidatos(as). Escreva um programa que calcule o(a) vencedor(a) da eleição. A votação ocorreu da seguinte maneira:
#Cada colaborador(a) votou em uma das quatro pessoas candidatas (que representamos pelos números 1, 2, 3 e 4).
##Ao final da votação, o programa deve exibir o número total de votos para cada candidato(a), os nulos e os votos em branco. Além disso, deve calcular e exibir a porcentagem de votos nulos em relação ao total de votos e a porcentagem de votos em branco em relação ao total de votos.
print("Votação da eleição!")
print("Escolha seu candidato(obs:apenas digitos numericos): ")
candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
branco = 0
nulo = 0
for colaborador in range (1,21):
    voto = int(input("candidato 1, candidato 2, candidato 3, candidato 4, aperte 5 para voto em branco e 6 para voto nulo. "))
    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 +=1
    elif voto == 3:
        candidato3 +=1
    elif voto == 4:
        candidato4 += 1
    elif voto == 5:
        branco += 1
    elif voto == 6:
        nulo += 1
    else: 
        print("Voto inválido tente novamente!")
print('RESULTADO DA VOTAÇÃO!')
print(f'candidato 1: {candidato1}')
print(f'candidato 2: {candidato3}')
print(f'candidato 3: {candidato3}')
print(f'candidato 4: {candidato4}')
print(f'votos nulo {nulo}')
print(f'votos em branco {branco}')
