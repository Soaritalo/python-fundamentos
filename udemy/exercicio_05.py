# Enunciado: quero que você itere uma string com while depois bote *x* em cada letra 
#
nome =  'italo Soares'
tamanho_nome = len(nome)

contador = 0
novo_nome = ''
while contador < len(nome):
    letra = nome[contador]
    novo_nome += f'*{letra}*'
    contador +=1
print(novo_nome)