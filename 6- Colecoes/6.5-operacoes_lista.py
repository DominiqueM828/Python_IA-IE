lista_inicial = ["Jonathan", "Yasmin", "Pamela"]
print("Lista inicial: ",lista_inicial)
print(80 * "-")

#=====Acrescentando Item na lista=========
lista_inicial.append("Victor")
print("Após o append(): ",lista_inicial)
print(80 * "-")

#=====Acrescentando Item em posição específica=========
lista_inicial.insert(3, "Dominique")
print("Após o insert(): ", lista_inicial)
print(80 * "-")

#====Modificando item na lista=========
lista_inicial[1] = "Paola"
print("Após a modificação: ",lista_inicial)
print(80 * "-")

#=====Deletando Indíce específico=========
del lista_inicial[0] 
print("Após del: ", lista_inicial)
print(80 * "-")

#=====Deletando valor específico=====
lista_inicial.remove("Dominique") 
print("Após remove: ", lista_inicial)
print(80 * "-")

#=====Apagando e armazenando valor da lista=========
removido = lista_inicial.pop(1)
print(f"Após pop, removido {removido}: ", lista_inicial)
print(80 * "-")

#=====Limpando a lista completa=========
lista_inicial.clear()
print("Após clear(): ", lista_inicial)
print(80 * "-")