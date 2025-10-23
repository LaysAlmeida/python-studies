teams = {}

def print_teams():
    print("Times listados:")
    for i, team in enumerate(teams.values(), start=1): # Enumerate retorna um objeto enumerado que combina um índice e o valor de cada elemento de um objeto iterável  
        print(f"{i}. {team['name']} (Jogadores: {len(team['players'])})")

# função para listar jogadores de um time
def print_team_players(team):
    print(f"Jogadores do {team['name']}:")
    for i, player in enumerate(team['players']):
        print(f"{i+1}. {player}")
        
option = 0       
while option !=7:
    print("O que você deseja fazer?")
    print("1. Adicionar um time")
    print("2. Remover um time")
    print("3. Listar times")
    print("4. Adicionar jogador em um time")
    print("5. Remover jogador em um time")
    print("6. Listar jogadores de um time")
    print("7. Sair")
    option = int(input("Digite aqui sua escolha: "))
    if option == 1:
        team_name = input("Digite o nome do time: ")
        teams[team_name] = {'name': team_name, 'players': []}
        print("Time adicionado.")
    elif option == 2:
        continue
    elif option == 3:
        print_teams()
    elif option == 4:
        continue
    elif option == 5:
        continue
    elif option == 6:
        continue
    elif option == 7:
        break
    else:
        print("Opção inválida. Tente novamente")
        break
