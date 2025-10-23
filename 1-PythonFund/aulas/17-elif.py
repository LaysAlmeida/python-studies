num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operation = input("Digite a operação a realizar (+ - * /): ")

if operation == '+':
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
else:
    print("Operação inválida. Tente novamente.")