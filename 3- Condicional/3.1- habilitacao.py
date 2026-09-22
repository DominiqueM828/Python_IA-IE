#Solicitando o nome e a idade do usuário
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

#Criando a condição caso for >= a 18 anos
if idade >= 18:
    possui_carteira = input("Possui carteira de motorista s/n: ")
    if possui_carteira == "s":
        print("Apto a dirigir")
    else:
        print("Não pode dirigir.")
else: 
    print("Menor de idade")