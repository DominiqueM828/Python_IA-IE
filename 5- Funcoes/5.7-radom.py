# Importando a biblioteca random
import random 

# Montando a variável e aplicar a biblioteca
def sortear(lista):
    return random.choice(lista)

# Criando a lista e executando o sorteio
nomes = ["Matheus", "Dominique", "João", "Pamela", "Giovena", "Alanis", "Lorena","Vitor", "Adriano", "Emily"]
print(sortear(nomes))