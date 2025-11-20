class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    
    def showEmployeeData(self):
        print(f"Nome: {self.name} - Salário: {self.__salary}")
        
bruno = Employee("Bruno", 4000)
lara = Employee("Lara", 3500)

bruno.showEmployeeData()
bruno.__salary(5000)  #Essa operação se torna impossível, pois __salary é um atributo privado 
bruno.name("Bruno Gomes") #Já isso aqui é possível, pois name é um atributo público     
lara.showEmployeeData()        