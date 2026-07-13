#Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos consecutivos e exiba o valor mais alto e mais baixo entre esses três anos.
valor_2023 = float(input('escreva o valor do carro em 2023: '))
valor_2024 = float(input('escreva o valor do carro em 2024: '))
valor_2025 = float(input('escreva o valor do carro em 2025: '))

if valor_2023 > valor_2024 and valor_2023 > valor_2025:
    maior = valor_2023
    print('o maior valor é o de 2023')

elif valor_2024 > valor_2025 and valor_2024 > valor_2023:
    maior = valor_2024
    print('o maior valor é o de 2024')

elif valor_2025 > valor_2023 and valor_2025 > valor_2024:
    maior = valor_2025
    print('o maior valor é o de 2025')

if valor_2023 < valor_2024 and valor_2023 < valor_2025:
    menor = valor_2023
elif valor_2024 < valor_2025 and valor_2024 < valor_2023:
    menor = valor_2024
else:
    menor = valor_2025

print(f'o maior valor é de {maior}')
print(f'o menor valor é o de {menor}')
input('pressione enter para sair')
