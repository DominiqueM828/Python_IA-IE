# Solicitando a idade e se é estudante ao usuário
idade = int(input("Digite sua idade:"))
estudante = input("Você é estudante s/n:")

#Verificando as informações do usuário
meia = (idade >= 60) or estudante == "s"

#Mostrando o resultado
print("Tem direito a meia-entrada:", meia)