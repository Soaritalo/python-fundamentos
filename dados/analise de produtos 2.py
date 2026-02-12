vendas = {
    'Produto A': [120, 150, 200, 180],
    'Produto B': [80, 90, 100, 110],
    'Produto C': [200, 210, 190, 220],
    'Produto D': [50, 60, 55, 65]
}
soma_ProdutoA = sum(vendas['Produto A'])
soma_ProdutoB = sum(vendas['Produto B'])
soma_ProdutoC = sum(vendas['Produto C'])
soma_ProdutoD = sum(vendas['Produto D'])
#1
print(f'{soma_ProdutoA}')
print(f'{soma_ProdutoB}')
print(f'{soma_ProdutoC}')
print(f'{soma_ProdutoD}')
#2
maximo = max(vendas,key=vendas.get)
print(f'O produto que teve maior faturamento total foi o: {maximo}')
#3
total_mes1 = vendas['Produto A'][0] + vendas['Produto B'][0] + vendas['Produto C'][0] + vendas['Produto D'][0]
total_mes2 = vendas['Produto A'][1] + vendas['Produto B'][1] + vendas['Produto C'][1] + vendas['Produto D'][1]
total_mes3 = vendas['Produto A'][2] + vendas['Produto B'][2] + vendas['Produto C'][2] + vendas['Produto D'][2]
total_mes4 = vendas['Produto A'][3] + vendas['Produto B'][3] + vendas['Produto C'][3] + vendas['Produto D'][3]
print(f'No 4 mes foi: {total_mes1}')
print(f'No 8 foi:     {total_mes2}')
print(f'no 12 foi:    {total_mes3}')
print(f'no 16 foi:    {total_mes4}')
totais = [total_mes1, total_mes2, total_mes3, total_mes4]
meses = ['Mês 1', 'Mês 2', 'Mês 3', 'Mês 4']
max_total = max(totais)
mes_max = meses[totais.index(max_total)]

print(f'O mês com o maior volume de vendas foi o {mes_max}, com total de {max_total} vendas.')
input('enter')
