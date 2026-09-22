# Solicitando a variável e as variáveis notas
nome = input("Digite seu nome: ")
nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))

#Calculando a média do estudante
media = (nota1 + nota2 + nota3 )/3

#Mostrando o resultado ao usuário
print("A média do aluno(a)", nome, "será ", media)