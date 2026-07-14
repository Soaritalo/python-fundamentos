# Enunciado:Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
# descrito, exiba a saudação apropriada. Ex.
# Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.


from datetime import datetime
entrada = input("Digite uma hora: ")
if ":" not in str(entrada):
    entrada += ":00"
hora = datetime.strptime(entrada, "%H:%M").time()
if ":" not in str(hora):
    hora += ":00"
def main():
    if hora.hour >= 4 and hora.hour <= 11:
        print('Bom dia')
    elif hora.hour >= 12 and hora.hour <= 17:
        print('Boa tarde')
    elif hora.hour >= 18 and hora.hour   <= 23:
        print('Boa noite')
    elif hora.hour >= 0 and hora.hour <= 3:
        print('Boa madrugada')
    else:
        print('Hora inválida. Digite um valor entre 0 e 23.')
main()
            
