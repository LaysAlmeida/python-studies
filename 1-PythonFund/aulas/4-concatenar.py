name = input("Digite o nome do jogo:\n")
yearLaunch = int(input("Digite o ano de lançamento: \n"))
gamePrice = float(input("Digite o valor do jogo: "))
supportMobileDevice = input("O jogo roda em dipositivos mobile(Tablet, Smartphone)? \n")

#Alternativa 1:
# print("###Dados do jogo###")
# print("===================")
# print("Nome do jogo:", name)
# print("Ano de lançamento:", yearLaunch)
# print("Preço: ", gamePrice)
# print("Roda em dispositivos mobile: ", supportMobileDevice)

#Alternativa 2:
# print("Nome do jogo:", name, "\nAno de lançamento:", yearLaunch,
#       "\nValor do jogo:", gamePrice, "\nFunciona em dispositivos mobile?", supportMobileDevice)

#Alternativa 3:
print(f"Nome do jogo: {name} \nAno do Lancamento: {yearLaunch} \nPreco: {gamePrice} \nRoda em dispositivos mobile? {supportMobileDevice}" )