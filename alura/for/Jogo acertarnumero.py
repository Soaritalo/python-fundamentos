for numeros in range (1,10):
    tentativa = int(input('Tente acertar o numero correto amiguinho!!: '))
    if tentativa == 10:
        print("vc acertou o numero!")
        print(f"(em apenas:{numeros} tentativas)")
        input('aperte enter para sair ')
        break
    elif tentativa > 10 or tentativa < 10 :
        print('vc errou amiguinho')
        continue
    
