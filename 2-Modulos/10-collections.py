from collections import Counter, namedtuple, deque
from operator import itemgetter

# 1 - Contar itens de uma lista
fruits = ["Maçã", "Pera", "Uva", "Morango", "Maçã", "Morango", "Uva"]
print(Counter(fruits))

# 2 - Utilizando tupla nomeada
game = namedtuple('game', ['name', 'price', 'note'])
g1 = game("Fifa 26", 299.0, 7.6)
g2 = game("Valorant", 0, 8.9)

print(g1)
print(g2)

#3 - Ordenando dicionários
studants = {"Bruno": 20, "Lays": 23, "Luke": 5, "Apolo": 1}
a = sorted(studants.items(), key=itemgetter(0))
print(studants)
print(a)

# 4 - Adicionando e removendo itens de uma fila em ambas extremidades
deq = deque([20, 40, 60, 80])
deq.appendleft(10)
deq.append(90)
print(deq)
deq.popleft()
deq.pop()
print(deq)