class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    
    def show_employee_data(self):
        print(f"Nome: {self.name} - Salário: {self.__salary}")
    
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary):
        self.__salary = salary
              
        
bruno = Employee("Bruno", 4000)
bruno.name = "Bruno Gomes"
bruno.showEmployeeData()
bruno.set_salary(5000)
bruno.showEmployeeData()
