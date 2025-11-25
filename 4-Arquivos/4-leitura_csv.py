with open("files/courses.csv", "r", encoding="utf-8") as file:
    for line in file:
        # row = line.rstrip().split(",")
        # print(f"{row[0]}-{row[1]}")
        #Outra forma
        language, category = line.rstrip().split(",")
        print(f"{language} -{category}")