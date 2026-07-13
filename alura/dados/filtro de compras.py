#Com os mesmos dados da questão anterior, defina quantas compras foram realizadas acima de 3000 reais e calcule a porcentagem quanto ao total de compras.
lista = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38,
         2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
soma = sum(lista)
quantidade= len(lista)
quantidade_acima = 0 
for gasto in lista:
    if gasto>3000:
        quantidade_acima+=1
porcentagem = (quantidade_acima / quantidade) * 100
print(f'A quantidade acima de 3000 é : {quantidade_acima} de {quantidade}')
print(f'A porcentagem é: {porcentagem}%')
input('Aperte enter para sair')
