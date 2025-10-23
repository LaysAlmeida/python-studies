gameInfo = {
    "name": "Minecraft",
    "yearLaunch": 2009,
    "gamePrice": 99.0,
    "classification": 9.0,
    "genre": ['Action', 'Adventure']
}
print(gameInfo)
print(len(gameInfo))
print(type(gameInfo))

# 1 - Recuperar um elemento do dicionário
print(gameInfo['genre'])
print(gameInfo.get('classification'))

# 2 - Buscar apenas as chaves do dicionário
print(gameInfo.keys())

# 3 - Buscar apenas os valores do dicionário
print(gameInfo.values())

# 4 - Buscar itens no dicionário com chave e valor
print(gameInfo.items())

# 5 - Adicionar itens no dicionário
gameInfo["players"] = 1
print(gameInfo)

# 6 - Atualizar itens no dicionário
gameInfo.update({"players": 1})
print(gameInfo)

# 7 - Remover itens do dicionário
gameInfo.pop("players")
print(gameInfo)