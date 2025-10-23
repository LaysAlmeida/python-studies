#1 - Função para imprimir Hello World
def welcome():
    print("Hello World!")
    
welcome()

#2 - Função para somar dois números
def sum(n1, n2):
    return (n1 + n2)

print(sum(6, 2))

#3 - Cadastrar um jogo   
def create_game(name, yearlauch, isGameFree):
    gameName = [name, yearlauch, isGameFree]
    print(gameName) 

create_game("Valorant", 2020, True)
create_game("Club Penguin", 2007, True)
