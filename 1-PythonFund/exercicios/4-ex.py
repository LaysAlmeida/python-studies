#Contagem regressiva e Beep no fim
import winsound
count = 10
while(count >= 0):
        print(count)
        count = count - 1
winsound.Beep(500, 500)

# #Tabuada
# num_mult = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# num = int(input("Digite o número para ver a tabuada: "))
# result = []

# for i in num_mult:
#     result.append(f"{num} x {i} = {num * i}")
# print(result)

# #Tabuada com List Comprehension
# resultado = [f"{num} x {i} = {num * i}" for i in num_mult]
# print(resultado)

#Tabuada com While
num = int(input("Digite o número para ver a tabuada: "))
num2 = int(input("Digite por de qual número você quer que comece a multiplicar: "))
num3 = int(input("Digite até e qual número você deseja multiplicar: "))
resul = []
while(num2 <= num3):
    resul.append(f"{num} x {num2} = {num * num2}")
    num2 += 1
    print(num2)
print(resul)