string = 'italo'
metodo = 'upper'

if getattr(string, 'upper'):
    print('tem upper')
    print(string.upper())
    print(getattr(string, metodo)())
else : print('nao tem metodo',metodo)