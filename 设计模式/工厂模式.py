#coding:utf-8

class Burger():
    name=""
    price=0.0

    def getPrice(self):
        return self.price
    def setPrice(self,price):
        self.price=price
    def getName(self):
        return  self.name
class cheeseBurger(Burger):
    def __init__(self):
        self.name="cheese burger"
        self.price=10.0

class spicyChickenBurger(Burger):
    def __init__(self):
        self.name="spicy chicken burger"
        self.price=15.0

class Snack():
    name=""
    price=0.0
    type="SNACK"
    def getPrice(self):
        return self.price
    def setPrice(self,price):
        self.price=price
    def getName(self):
        return self.name

class chips(Snack):
    def __init__(self):
        self.name="chips"
        self.price=6.0

class chickenwings(Snack):
    def __init__(self):
        self.name="chicken wings"
        self.price=12.0

class Beverage():
    name=""
    price=""
    type="BEVERAGE"
    def getPrice(self):
        return self.price
    def setPrice(self,price):
        self.price=price
    def getName(self):
        return  self.name

class coke(Beverage):
    def __init__(self):
        self.name="coke"
        self.price=4.0

class milk(Beverage):
    def __init__(self):
        self.name="milk"
        self.price=5.0

class foodFactory():
    type=""
    def createFood(self,foodClass):
        print self.type,"factory produce a instance"
        foodIns=foodClass()
        return foodIns
class burgerFactory(foodFactory):
    def __int__(self):
        self.type="BURGER"
class snackFactory(foodFactory):
    def __int__(self):
        self.type="SNACK"
class beverageFactory(foodFactory):
    def __int__(self):
        self.type="BEVERAGE"

if __name__=="__main__":
    burger_factory=burgerFactory()
    snack_factory=snackFactory()
    beverage_factory=burgerFactory()
    
    cheese_burger=burger_factory.createFood(cheeseBurger)
    print cheese_burger.getName(),cheese_burger.getPrice()