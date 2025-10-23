gamesSet = {"Spider Man Remastered", "Hogwarts Legacy", 
             "Split Fiction", "Red Dead Redemption 2", 
             "Rainbow Six Siege", "It Takes Two"}

print(gamesSet)

# 1 - Buscar o tamanho do set
print(len(gamesSet))

# 2 - True e 1 são o mesmo valor
exampleSet = {"Hogwarts Legacy", 1, 100.0, True}
print(exampleSet)

#3 - Adicionar item de outro set
gamesSet.update(exampleSet)
print(gamesSet)

#4 - Remover um item do set
gamesSet.remove("Rainbow Six Siege")
print(gamesSet)
gamesSet.remove("Red Dead Redemption 2")
print(gamesSet)