# Solicitando o peso e a altura ao usuário
peso = float(input("Digite seu peso em (Kg): "))
altura = float(input("Digite sua altura em (M): "))

# Calculando o IMC do usuário
imc = peso/altura**2

#Apresentando ao usuário o resultado do IMC
print("O seu IMC é: ", imc)