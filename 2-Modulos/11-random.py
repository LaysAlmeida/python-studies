import random

# 1 - Seleciona um valor aleatório de uma lista
list1 = [6, 1, 7, 2, 8, 3, 5, 9]
print(random.choice(list1))

# 2 - Gera um número aleatório em um intervalo de valores
r1 = random.randint(5, 15)
print(r1)

#3 - Seleciona caractere aleatório de uma string
name = "Bruno Gomes"
r2 = random.choice(name)
print(r2)

# 4 - Seleciona mais de um valor aleatório
#Sintaxe: random.sample(sequencia, tamanho)
print(random.sample(list1, 2))
s = "Bruno Gomes"
print(random.sample(s, 5))