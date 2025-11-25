with open("files/names.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(f"{line.rstrip()}") #Remove os espaços em branco