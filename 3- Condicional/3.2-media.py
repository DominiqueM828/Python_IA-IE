# Pedindo as informações dos estudades e suas notas
nome = input("Digite o nome do aluno:")
nota = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))

# Calculando a média dos estudantes
media = (nota + nota2 + nota3)/ 3

# Realizando a separação das médias
if media < 4:
    situacao = "Reprovada!"
elif media <= 6:
    situacao = "Em recuperação!"
else:
    situacao = "Aprovado!"

print(f"A média do aluno(a) {nome} é {media:.2f} e está: {situacao}")