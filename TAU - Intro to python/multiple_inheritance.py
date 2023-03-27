# Parent class 1

class Item():
    def __init__(self, sku) :
        self.sku = sku

    def print_sku(self):
        print("The sku is {}.".format(self.sku))

#Parent class 2
class Garment():
    def __init__(self, type, section) :
        self.section = section
        self.type = type

    def print_garment(self):
        print("The garment is in section {}, {}.".format(self.section,self.type))

# Child Class
class Shirts(Item,Garment):
    def __init__(self, sku, section, type, name, color):
        self.name = name
        self.color = color
        Item.__init__(self,sku)
        Garment.__init__(self,type,section)

    def print_shirt(self):
        print("{} {} on sale!".format(self.color,self.name))

tshirt = Shirts("0001",43,"Tops","T-shirt","black")
tshirt.print_sku()
tshirt.print_garment() 
tshirt.print_shirt()