# 1 - Função que recebe nome e sobrenome
def full_name(fname, lname):
    print(f"Nome completo: {fname} {lname}")
    
full_name("Bruno", "Gomes")

#2 - Somar dois valores
def sum(n1, n2):
    return (n1 + n2)

print(sum(10, 8))

#3 - Argumentos default numa função
def address(country = "Brasil"):
    print(f"Eu moro no {country}")
    
address()    
address("Canadá")    

#4 - Avaliação do jogo
def rating_game(qtdRating):
    game_name = input("Digite o nome do jogo: ")
    sum = 0
    for i in range(qtdRating):
        note = float(input("Digite a nota para o jogo: "))
        sum += note
    print(f"Média de avaliação do jogo {game_name} é {sum / qtdRating}")
    
rating_game(5) #Passa a quantidade de notas que aquele jogo tem         
        