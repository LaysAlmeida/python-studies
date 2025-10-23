gamesList = ["Spider Man Remastered", "Hogwarts Legacy", 
             "Split Fiction", "Red Dead Redemption 2", 
             "Rainbow Six Siege", "It Takes Two"]

#1 - Contar o tamanho da lista
print(len(gamesList))

#2 - Recuperar um item da lista pelo índice
print(gamesList.index("Split Fiction"))

#3 - Adiciona um item no fim da lista
gamesList.append("GTA V")
print(gamesList)

#4 - Ordenar a lista
gamesList.sort()
print(gamesList) #Nesse caso ordena em ordem alfabética

#5 - Copiar os itens de uma lista para outra
gameReset = gamesList.copy()
gameReset.remove("GTA V")
print(gameReset)

#6 - Remove todos os itens da lista
gamesList.clear()
print(gamesList)