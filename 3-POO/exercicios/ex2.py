class Product:
    def __init__(self, productName, productPrice):
        self.name = productName
        self.price = float(productPrice)
        self.discountValue = 0
        self.totalDiscount = 0
    
    def __str__(self):
       return f"Produto: {self.name} - R${self.price}"

    def discount(self, discountAmount):
        self.discountValue =+ discountAmount
        self.totalDiscount =+ (self.price - ((discountAmount / 100) * self.price))
    def productInfo(self):
        print("### Informações do Produto ###")
        print(f"Produto: {self.name} - R${self.price}")
        if self.discountValue > 0:
             print(f"Preço com desconto de {self.discountValue}%: \n{self.name} - R${self.totalDiscount:.2f}")
        else:
            print("Produto sem desconto.")
        print("###### Fim da descrição ######")    
        
telescopio = Product("Telescópio", 500)
telescopio.discount(15)
telescopio.productInfo()

gel = Product("Gel de cabelo", 20)
gel.discount(0)
gel.productInfo()