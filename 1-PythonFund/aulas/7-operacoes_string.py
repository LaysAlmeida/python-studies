gameDescription = """
    Fifa 25 é um jogo de futebol 
    desenvolvido pela EA Sports
    e que possibilita jogar localmente ou online
"""

gameName = "Fifa "
gameVersion = "25"
# 1 - Concatenação de Strings
gameFullName = gameName + gameVersion
print(gameFullName)

# 2 - Operação de multiplicação de Strings
line = "="
print(line * 25)

# 3 - Procurar uma palavra dentro de um texto
print("Fifa" in gameDescription)
print("fifa" in gameDescription)
print("futebol" in gameDescription)