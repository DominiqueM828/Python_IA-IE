# Craindo a funcao maior numero
def maior_numero(x,y):
    if x > y:
        return x
    else:
        return y
    
#Solicitando ao usuario dois numeros
num_1 = float(input("Digite um numero: "))
num_2 = float(input("Digite outro numero: "))

# Chamando a funcao de verificacao
resultado = maior_numero(num_1, num_2)

# Apresentando ao usuario os resultados
print(f"O maior numero digitado foi: {resultado}")