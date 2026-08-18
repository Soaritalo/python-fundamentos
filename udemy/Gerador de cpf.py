import random
def gerador_de_cpf():
    base = [random.randint(0,9) for  in range(9)]
    return base

def validador_de_cpf(quantidade):
    resultado = []
    for _ in range(quantidade):
        verificacao = [ 10 , 9 , 8 , 7 , 6 ,5 , 4,  3 , 2]
        cpf = gerador_de_cpf()
        digitos = []

        for i in range(2):
            peso = 10 + i          
            qtd = 9 + i            
            soma = 0
            for j in range(qtd):
                soma += cpf[j] * (peso - j)

            correcao = (soma * 10) % 11
            if correcao > 9:
                correcao = 0
            digitos.append(correcao)
            cpf.append(correcao)

        validado = "".join(str(d) for d in cpf)
        resultado.append(validado)
    return(resultado)
print("Cpf`s validados:", validador_de_cpf(5))