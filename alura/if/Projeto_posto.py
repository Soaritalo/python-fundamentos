 #Um estabelecimento está vendendo combustíveis com descontos variados. Para o etanol, se a quantidade comprada for até 15 litros, o desconto será de 2% por litro. Caso contrário, será de 4% por litro. Para o diesel, se a quantidade comprada for até 15 litros, o desconto será de 3% por litro. Caso contrário, será de 5% por litro. O preço do litro de diesel é R$ 2,00 e o preço do litro de etanol é R$ 1,70. Escreva um programa que leia a quantidade de litros vendidos e o tipo de combustível (E para etanol e D para diesel) e calcule o valor a ser pago pelo cliente. Tenha em mente algumas dicas:

#O do valor do desconto será a multiplicação entre preço do litro, quantidade de litros e o valor do desconto.
#O valor a ser pago por um cliente será o resultado da multiplicação do preço do litro pela quantidade de litros menos o valor de desconto resultante do cálculo.
#Diesel, etanol 
# etanol o desconto é de se for ate 15 litros 2% por litro maior que 15 é 4%
# diesel o desconto é de 3% se for maiorque 15  5% por litro 
preço_diesel = 2.00 
preço_etanol = 1.70
input('Bem vindo a loja!! ')
quantidade_diesel = float(input(' Digite a quantidade de litros de diesel que deseja comprar: '))
quantidade_etanol = float(input(' Digite a quantidade de litros de etanol que deseja comprar: '))

total_diesel = quantidade_diesel * preço_diesel
total_etanol = quantidade_etanol * preço_etanol
if quantidade_diesel < 0  or quantidade_etanol < 0 :
    print('ta duro dorme')
    input('aperte enter para sair')
    exit()
if quantidade_diesel > 15:
    desconto_diesel = total_diesel * 0.95
else:
    desconto_diesel = total_diesel * 0.97
if quantidade_etanol > 15:
    desconto_etanol = total_etanol * 0.95
else:
    desconto_etanol= total_etanol * 0.97
print(f'O total de diesel deu {desconto_diesel}R$')
print(f'O total de etanol deu {desconto_etanol}R$')
input('aperte enter para sair')
