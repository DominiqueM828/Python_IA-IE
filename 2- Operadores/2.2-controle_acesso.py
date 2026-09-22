# Solicitando as informações do usuário
idade = int(input("Digite sua idade:"))
altura = float(input("Digite sua altura:"))

#Validando o acesso à Montanha-Russa
acesso = (idade >= 12) and altura >= 1.40 

#Apresentando a validação ao usuário
print("Divirta-se: ", acesso)