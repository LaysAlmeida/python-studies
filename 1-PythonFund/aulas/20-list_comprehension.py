#1 - Listar os valores de 0 a 10 que sejam menores que 4
for i in range(10):
    if i < 4:
        print(i)

# 1.1 - Outra forma de fazer utilizando List Comprehension e o retorno é no formato de Lista
listNumbers = [i for i in range(10) if i < 4]
print(listNumbers)

# 2 - Lista os jogos que possuam a letra a
gamesList = ["Spider Man Remastered", "Hogwarts Legacy", "Red Dead Redemption 2", "Transformice", "Split Fiction", "COD"]

newList = [gamesWithA for gamesWithA in gamesList if "a" in gamesWithA]
print(newList)

#2.1 - Mesma funcionalidade, mas usando for e if
for games in gamesList:
    if "a" in games:
        print(games)
        
#3 - Retornar jogos ainda não zerados
gamesFinished = [x for x in gamesList if x != "COD"]   
print(gamesFinished)  

#3.1 - Mesmo exemplo, mas usando o for
for i in gamesList:
    if i != "COD":
        print(i)
        
#4 - Dobrar o valor de um produto com for
lista_precos = [500, 1500, 2000, 100, 25]
nova_lista = []
for double in lista_precos:
  nova_lista.append(double * 2)
print(nova_lista)

# 4.1 - Dobrar com List Comprehension
newList = [d * 2 for d in lista_precos]
print(newList)

# 5 - 50% de imposto em produtos acima de 1000 dólares
final_price = []
for price in lista_precos:
    if price > 1000:
        final_price.append(price * 0.5)
print(final_price)

#5.1 - Com List Comprehension
new_price = [p * 0.5 for p in lista_precos if p > 1000]
print(new_price)