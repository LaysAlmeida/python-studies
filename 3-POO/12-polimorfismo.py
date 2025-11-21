class Device:
    def __init__(self, brand, model_name, price, ram, internal_memory, back_camera):
        self._brand = brand
        self._model_name = model_name
        self._price = price
        self.ram = ram
        self.internal_memory = internal_memory
        self._back_camera = back_camera

    @staticmethod
    def make_a_call(phone_num):
        print(f"calling {phone_num}...")
       
    def __str__(self):
        return f"{self._brand} {self._model_name}"
    
    def discount(self):
        return self._price * 0.85

class SmartPhone(Device):
    def discount(self):
        return self._price * 0.90
      
class Tablet(Device):
    def discount(self):
        return self._price * 0.80          

Iphone = SmartPhone('Iphone','13',7000,'4GB','128GB','25MP')
print(Iphone)
print(f"Valor do {Iphone._brand} {Iphone._model_name} com desconto é R${Iphone.discount():.1f}")
print(vars(Iphone))   

Ipad = Tablet('Ipad', 'Air', 7499, '6BG', '256GB', '12MP')
print(Ipad)
print(f"Valor do {Ipad._brand} {Ipad._model_name} com desconto é R${Ipad.discount():.1f}")
print(vars(Ipad))