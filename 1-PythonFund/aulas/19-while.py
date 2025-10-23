gamesList = ["Spider Man Remastered", "Hogwarts Legacy", "Red Dead Redemption 2", "Transformice"]
gameName = input(f"Digite o nome de um dos jogos abaixo para fazer 5 avaliações \n {gamesList}: ")
qtdRating  = 0 # Quantidade de notas
totalRating = 0 # Soma das notas
rating = 0 # Nota
average = 0 # Média das notas

while(qtdRating < 5):
    rating = float(input(f"Informe a nota que deseja dar para {gameName}: "))
    if(rating < 0): 
        print("Nota inválida. Tente novamente")
        continue
    totalRating = totalRating + rating
    qtdRating = qtdRating + 1
    average = totalRating / qtdRating 
print(f"A média das avaliações de {gameName} é {average}")