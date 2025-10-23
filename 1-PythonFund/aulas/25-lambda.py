# 1 - Função de potência de um número
power = lambda num: num ** 2
print(power(2))

# 2 - Função que verifica se um número é par
pair = lambda num: num % 2 == 0
print(pair(25))
print(pair(24))

# 3 - Divisão de um número
divNum = lambda num, num2: num / num2
print(divNum(4, 2))

# 4 - Função que inverte uma string
reverse = lambda s: s[::-1]
print(reverse("Bruno"))