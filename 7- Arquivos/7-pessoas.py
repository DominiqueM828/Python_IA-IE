#Solicitando o nome e o email.com
nome = input("Digite seu nome: ")
email = input("Digite seu email: ")

#Montando o arquivo.txt com Python
arquivo = open("7-pessoas.txt", "a", encoding="utf-8")
arquivo.write(f"{nome} | {email} \n")
arquivo.close()

#Forma reduzida de se fazer
with open("7-pessoas.txt","a", encoding="utf-8") as arquivo:
    arquivo.write(f"{nome} | {email} \n")