# Criando a função verificar idade
def verificar(idade):
    if idade >=18:
        return "Maior de idade!"
    else:
        return "Menor de idade!"

#Pedindo ao usuário sua idade
idade_usuário = int(input("Digite sua idade: "))
resultado = verificar(idade_usuário)

# Apresentando o resultado ao usuário
print(resultado)