#Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A ultrapassar ou igualar a colônia de uma bactéria B, com base nas taxas de crescimento de 3% e 1,5% respectivamente. Considere que a colônia A inicia com 4 elementos e a B com 10.
COLONIA_A = 4
COLONIA_B = 10
taxa_crescimento_A = 0.03
taxa_crescimento_B = 0.015
dias = 0
while COLONIA_A < COLONIA_B:
    COLONIA_A = COLONIA_A + (COLONIA_A * taxa_crescimento_A)
    COLONIA_B = COLONIA_B + (COLONIA_B * taxa_crescimento_B)    
    dias += 1
print(f'Levará {dias} dias para a colônia A ultrapassar ou igualar a colônia B.')
