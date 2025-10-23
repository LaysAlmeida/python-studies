print("####################################")
print("Antecessor e sucessor de um número:")
print("####################################")
num = int(input("Digite um número: "))

antecessor = num - 1;
sucessor = num + 1

print(f"O antecessor de {num} é: {antecessor} e o sucessor é {sucessor}")

print("####################################")
print("Média de 4 notas")
print("####################################")

note1 = float(input("Digite a primeira nota: "))
note2 = float(input("Digite a segunda nota: "))
note3 = float(input("Digite a terceira nota: "))
note4 = float(input("Digite a quarta nota: "))

average = (note1 + note2 + note3 + note4) / 4

print(f"A média das notas foi de: {average}")