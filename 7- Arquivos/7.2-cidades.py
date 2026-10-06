import csv

dados_tabela =[
    ["BAIRRO", "CIDADE", "ESTADO", "CEP"],
    ["Jardim Belval", "Barueri", "SP", "06654890"],
    ["Miraflor", "Itapevi", "SP", "07654346"],
    ["Santa Rita", "Itapevi", "SP", "06654876"],
    ["Centro", "Osasco", "SP", "087652290"],
]

with open("7.02-cidades.csv", "w", encoding="utf-8", newline="") as arquivo_csv:
    escrevendo = csv.writer(arquivo_csv)
    escrevendo.writerows(dados_tabela)