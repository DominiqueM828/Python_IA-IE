# Solicitando ao usário a renda e situação do correntista
renda = float(input("Digite a sua renda mensal R$:"))
situacao = input("Possui restrição / nome negativado s/n:")

#Validando a situação de restrição
emprestimo = (renda >= 3000) and situacao == "n" 

print("Emprestimo Aprovado: ", emprestimo)