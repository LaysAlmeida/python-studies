class Console:
    def __init__(self, name, price):
        self.gameName = name
        self.gamePrice = price
    
    @classmethod
    def from_text(cls, string):
        import re
        item = re.findall("é \w*", string)
        name = item[0][2:]
        price = item[1][2:]
        return cls(name, int(price))

ps5 = Console.from_text("Meu video game é PS5 e o preço é 3500 reais")
print(ps5.__dict__)