import pprint

myFavGames = {
    "valorant": {
        "yearLaunch": 2020,
        "classification": 8.5,
        "genre": ["ação", "fps"]
    },
    "transformice": {
        "yearLaunch": 2010,
        "classification": 9.0,
        "genre": ["MMO"]
    },
    "club penguin": {
        "yearLaunch": 2005,
        "classification": 9.0,
        "genre": ["MMORPG"]
    }
}

pp = pprint.PrettyPrinter(depth=4)

pp.pprint(myFavGames)

# 1 - Buscar informação dentro de um dicionário aninhado
print(myFavGames["valorant"]["genre"])

# 2 - Adicionar novo item
myFavGames["club penguin"]["players"] = 1
print(myFavGames["club penguin"])

# 3 - Excluir um dicionário
del myFavGames["transformice"]
pp.pprint(myFavGames)