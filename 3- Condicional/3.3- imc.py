# Solicitando os dados do paciente
nome = input("Digite o nome do paciente:")
peso = float(input("Digite o peso em (Kg) do paciente: "))
altura = float(input("Digite a altura em (M) do paciente: "))

# Calculando o IMC do paciente
imc = peso/altura**2

# Realização do quadro do paciente
if imc < 18.5:
    situacao = "Abaixo do peso"
elif imc <= 24.9:
    situacao = "Peso Adequado"
elif imc <= 29.9:
    situacao = "Sobrepeso"
elif imc <= 34.9:
    situacao = "Obesidade Grau I"
elif imc <= 39.9:
    situacao = "Obesidade Grau II"
else:
    situacao = "Obesidade Grave"

print(f"O(A) paciente {nome} tem seu imc {imc:.2f} e sua situação se encontra em {situacao}")