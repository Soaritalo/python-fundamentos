    #Em uma empresa de venda de imóveis você precisa criar um código que analise os dados de vendas anuais para ajudar a diretoria na tomada de decisão. O código precisa coletar os dados de quantidade de venda durante os anos de 2022 e 2023 e fazer um cálculo de variação percentual. A partir do valor da variação, deve ser enviada às seguintes sugestões:

    #Para variação acima de 20%: bonificação para o time de vendas.
    #Para variação entre 2% e 20%: pequena bonificação para time de vendas.
    #Para variação entre 2% e -10%: planejamento de políticas de incentivo às vendas.
    #Para variação abaixo de -10%: corte de gastos.
    dado2022 = float(input('Digite os dados de quantidade de venda durante 2022: '))
    dado2023 = float(input('Digite os dados de quantidade de venda durante 2023: '))
    variaçao = (dado2023 - dado2022) / dado2022
    if variaçao > 0.2:
        print('Bonificaçao pro time de vendas!!! ')
        input('aperte enter para sair ')
    elif  0.02 <= variaçao <= 0.2:
        print('pequena bonificaçao para o time de vendas !')
        input('aperte enter para sair ')
    elif  0.02 > variaçao  >= -0.10:
        print('Planejamento de politicas de incentivo as vendas')
        input('aperte enter para sair ')
    elif variaçao < -0.10:
        print('corte de gastos')
        input('aperte enter para sair ')

