#Cáculo de distância:

tripDistance = float(input("Qual é a distância em km que você deseja percorrer? "))

if tripDistance <= 200:
    tripPrice = tripDistance * 0.5
else:
    tripPrice = tripDistance * 0.35
    
print(f"O valor da sua viagem é de R${tripPrice:.2f}")

#Aumento salário funcionário
employeeSalary = float(input("Informe o seu salário atual: "))

if employeeSalary <= 1250.0:
     salaryIncrease = employeeSalary * 1.15
     print("Você teve um aumento de 15% no seu salário!")
else:
    salaryIncrease = employeeSalary * 1.1
    print("Você teve um aumento de 10% no seu salário!")
   
print(f"Seu salário era R${employeeSalary:.2f} e agora é de R${salaryIncrease:.2f}")