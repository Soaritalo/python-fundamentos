pares = []
impar = []

for IDs in range (1,11):
    ID = int(input('Digite O ID do produto: '))
    if  ID < 0:
        continue
    resultado1 = ID % 2 
    if resultado1 == 1:
        impar.append(ID)
    else:
        pares.append(ID)
print(f'Foram {len(pares)} produtos doces!')
print(f'Sendo eles:{pares} produtos doces!')
print(f'Foram {len(impar)} produtos amargos!')   
print(F'Sendo eles: {impar} produtos amargos!')
input('aperte enter para sair')
