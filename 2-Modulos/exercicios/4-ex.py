import random
userChoice = True
while userChoice:
   userChoice = input("Você deseja advinhar o número? \n1- Sim \n2- Sair\n")
   if userChoice == "1":
        numberUser = int(input("Escolha um número entre 0 e 10: "))
        numberRandom = random.randint(0, 10)
        if numberUser == numberRandom:
            print(f"Parabéns, você acertou! O número era {numberRandom} e você escolheu {numberUser}.")
        else:
            print(f"Tente novamente. O número era {numberRandom} e você escolheu {numberUser}.")
   elif userChoice == "2":
        userChoice = False