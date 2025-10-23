# 1 - Soma de números
def sum(*num):
    sum_total = 0
    for n in num:
        sum_total = sum_total + n
    print(sum_total)

sum(10)
sum(10, 8)
sum(10, 8, 12)

# 2 - Apresentação de cursos
def presentation(**data):
    for key, value in data.items(): #items() pega tanto a chave quanto o valor, por isso dois argumentos ali
        print(f"{key}: {value}")

presentation(courseName= "Python", category = "Backend", level="Beginner")
presentation(courseName= "JavaScript", category = "Frontend", level="Beginner")