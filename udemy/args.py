def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total



digitado  = input("Digite numeros: ")   
partes  = digitado.split()              
numeros   = [int(_) for _ in partes]    
resultado = soma(*numeros)              
print(resultado)