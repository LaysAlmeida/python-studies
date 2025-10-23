gamesList = ["Spider Man Remastered", "Hogwarts Legacy", "Red Dead Redemption 2", "Transformice"]

# 1 - Iterando itens de uma lista
for game in gamesList:
    print(game)
    
# 2 - Utilizando break para interromper o loop
for game in gamesList:
    if game == "Hogwarts Legacy":
        break
    print(game)
    
# 3 - Utilizando continue para ir para a próxima iteração quando condição for atendida
for game in gamesList:
    if game == "Hogwarts Legacy":
        continue
    print(game)
    
# 4 - Média de avaliação de um jogo
gameRated = gamesList[1]
gameRating = int(input(f"Digite quantas avaliações você deseja dar para {gameRated}: "))
sumRating = 0
for game in range(gameRating):
    note = float(input("Digite em quantas estrelas você avalia o jogo: "))
    sumRating = sumRating + note
print(f"A média de avaliação de {gameRated} é {(sumRating)/gameRating}")