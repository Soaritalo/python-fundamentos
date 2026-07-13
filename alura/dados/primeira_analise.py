import pandas as pd

dados = {
    "produto": ["Vidro", "Farol", "Retrovisor"],
    "vendas": [120, 80, 45]
}

df = pd.DataFrame(dados)

print(df)
print("\nTotal de vendas:", df["vendas"].sum())
