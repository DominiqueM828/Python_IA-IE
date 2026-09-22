#Iniciando o registro e situação:
nome = input("Digite o nome do paciente:")
idade = int(input("Digite a idade do paciente:"))

#Classificando a idade do paciente
if idade >= 65:
    classificacao = "Vintage"
elif idade >=31:
    classificacao = "Adulto"
elif idade >= 15:
    classificacao = "Jovem"
elif idade >= 11:
    classificacao = "Adolescente"
elif idade >= 4:
    classificacao = "Criança"
elif idade >= 1:
    classificacao = "Bebê"
else:
    classificacao = "Recém nascido"

print(f"O(A) paciente {nome} se encontra na classificação {classificacao}")