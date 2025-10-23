#Conta letras maiúsculas e minúsculas
def countLetters (text):
    counterMin = 0
    counterMai = 0
    for l in text:
        if l.isupper():
            counterMai += 1
        elif l.islower():
            counterMin += 1
    return (f"'{text}' tem {counterMai} letras maiúsculas e {counterMin} minúsculas")

print(countLetters("Eu te amo Bruno Gomes"))            

#Lista números pares e ímpares de uma lista
numbers_list = [4, 9, 10, 2, 5, 8, 19, 3, 1]
pares = []
impares = []

for n in numbers_list:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(f"Os números pares são: {pares}")        
print(f"Os números pares são: {impares}")

#Mesma coisa mas em métodos
def check_numbers(numbers):
    pairs = []
    odd = []
    for n in numbers:
        if n % 2 == 0:
            pairs.append(n)
        else:
            odd.append(n)
    return pairs, odd

print(check_numbers([2, 6, 8, 0, 1, 3, 9, 17]))            