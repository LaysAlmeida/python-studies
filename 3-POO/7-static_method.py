class Course:
    def __init__(self, name, trail):
        self.courseName = name
        self.trail = trail
        
    @staticmethod
    def courses_trail(trail):
        if trail == "Python Fundamentos":
            courses = ["Dominando o Python", "Módulos e Pip", "Orientação a Objetos"]
        elif trail == "Automação com Python":
            courses = ["Automação de Tarefas", "Web Scraping", "Assistente virtual em Python"]
        else:
            courses = ["A definir"]
        return courses

print(Course.courses_trail("Python Fundamentos"))
print(Course.courses_trail("Automação com Python"))
print(Course.courses_trail("Análise de Dados"))       