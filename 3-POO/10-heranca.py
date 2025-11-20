class Animal():
    def __init__(self, name, size, color, race):
        self.name = name
        self.size = size
        self.color = color
        self.race = race
    
    def comer(self):
        print("Comendo...")
    
    def animal_characteristics(self):
        print(f"Nome: {self.name} \nTamanho: {self.size}cm \nCor: {self.color} \nRaça: {self.race} ")  
        
class Horse(Animal):
    saddle = True
    
    def escape(self):
        print("Cavalo fugindo...")
        
class Lion(Animal):
    mane = True
    
    def hunt(self):
        print("Caçando...") 

h = Horse("Tracey", 210, "Brown", "SRD") #É possível passar esses parâmetros, pois eles são herdados da classe pai (Animal)
h.animal_characteristics() #A mesma coisa se aplica a esse método
h.comer()#A mesma coisa se aplica a esse método
h.escape() #Método próprio da class Horse

l = Lion("Simba", 200, "White", "SRD" )
l.animal_characteristics()
l.hunt()
l.comer()