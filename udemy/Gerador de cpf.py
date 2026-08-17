import random
def gerador_de_cpf():
    base = [random.randint(0,9) for _ in range(9)]
    return base

# print(gerador_de_cpf())

def validador_de_cpf(quantidade):
    resultado = []
    for _ in range(quantidade):
        verificacao = [ 10 , 9 , 8 , 7 , 6 ,5 , 4,  3 , 2]
        cpf = gerador_de_cpf()
    # cpf = cpf.replace("-", "").replace(".", "")
    # lista = [int(c) for c in cpf]
        digitos = []

        for i in range(2):
            peso = 10 + i          # começa em 10, depois em 11
            qtd = 9 + i            # usa 9 dígitos, depois 10
            soma = 0
            for j in range(qtd):
                soma += cpf[j] * (peso - j)

            correcao = (soma * 10) % 11
            if correcao > 9:
                correcao = 0
            digitos.append(correcao)
            cpf.append(correcao)

        # print(digitos)
        validado = "".join(str(d) for d in cpf)
        resultado.append(validado)
        # print(f"CPF original: {cpf}")
        # print(f"CPF validado: {validado}")
        # if cpf == validado:
        #         print('CPF Validado!!')
        # else :
        #         print('CPF Invalido!!!!!!')
    return(resultado)
print("Cpf`s validados:", validador_de_cpf(5))