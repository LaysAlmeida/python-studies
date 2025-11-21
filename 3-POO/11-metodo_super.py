class Phone:
    def __init__(self, brand, model_name, price):
        self._brand = brand
        self._model_name = model_name
        self._price = price
    
    @staticmethod
    def make_a_call(phone_num):
        print(f"calling {phone_num}...")
       
    def __str__(self):
        return f"{self._brand} - {self._model_name}"

class SmartPhone(Phone):
    def __init__(self, brand, model_name, price, ram, internal_memory, back_camera):
       super().__init__(brand, model_name, price)    
       self.ram = ram
       self.internal_memory = internal_memory
       self.back_camera = back_camera

Iphone = SmartPhone('Iphone','13',7000,'4GB','128GB','25MP')
print(Iphone)
Iphone.make_a_call(32142342)
print(vars(Iphone)) # retorna um dicionário de atributos de um objeto   