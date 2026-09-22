#Criando a função nome completo
def nome_completo (nome, sobrenome):
    return f"{nome} {sobrenome}"

#Solicitando ao usuário seu nome e sobrenome
first_name = input("Digite seu nome: ")
last_name = input("Digite seu sobrenome: ")

#Chamando a função e formando o nome inteiro
nome_inteiro = nome_completo(first_name, last_name)

#Apresentando as boas-vindas ao usuário
print(f"Seja bem-vindo(a), {nome_inteiro}")