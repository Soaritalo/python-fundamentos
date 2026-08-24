# "
# Calculo do primeiro dígito do CPF
# CPF: 746.824.890-70
# Colete a soma dos 9 primeiros dígitos do CPF
# multiplicando cada um dos valores por uma
# contagem regressiva começando de 10

# Ex.:  746.824.890-70 (746824890)
#    10  9  8  7  6  5  4  3  2
# *  7   4  6  8  2  4  8  9  0
#    70  36 48 56 12 20 32 27 0

# Somar todos os resultados: 
# 70+36+48+56+12+20+32+27+0 = 301
# Multiplicar o resultado anterior por 10
# 301 * 10 = 3010
# Obter o resto da divisão da conta anterior por 11
# 3010 % 11 = 7
# Se o resultado anterior for maior que 9:
#     resultado é 0
# contrário disso:
#     resultado é o valor da conta
# O primeiro dígito do CPF é 7

verificacao = [ 10 , 9 , 8 , 7 , 6 ,5 , 4,  3 , 2]
cpf = input("Digite um cpf valido: ")
cpf = cpf.replace("-", "").replace(".", "")
# cpf = '15497149707'
if not cpf.isdigit():
    print("Digite um NUMERO!")
else:
    lista = [int(c) for c in cpf]
    digitos = []

    for i in range(2):
        peso = 10 + i          # começa em 10, depois em 11
        qtd = 9 + i            # usa 9 dígitos, depois 10
        soma = 0
        for j in range(qtd):
            soma += lista[j] * (peso - j)

        correcao = (soma * 10) % 11
        if correcao > 9:
            correcao = 0
        digitos.append(correcao)

print(digitos)
validado = cpf[:9] + str(digitos[0]) + str(digitos[1])
print(f"CPF original: {cpf}")
print(f"CPF validado: {validado}")
if cpf == validado:
            print('CPF Validado!!')
else :
      print('CPF Invalido!!!!!!')