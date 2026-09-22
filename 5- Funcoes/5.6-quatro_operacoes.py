# Criando as funcoes aritmeticas
def  somar (x,y ):
   return x + y
def subtrair (x, y):
   return x - y
def multiplicar(x,y):
  return  x * y 
def dividir(x,y):
  return x / y 

num1 = float(input("Digite um numero: "))
num2 = float(input("Digite outro numero: "))

resultado = somar (num1, num2 ), subtrair (num1, num2), multiplicar(num1,num2), dividir(num1,num2)

print("Seus resultados são: {resultado}")