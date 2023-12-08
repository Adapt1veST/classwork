class Animal:
    def __init__(self, anames = "Cat"):
        self.aname = anames
class Human:
    def __init__(self, name="Human"):
        self.name = name
class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passangers = []        
    def add_passanger(self, human, aname):
        self.passangers.append(human, aname)
    def print_passangers_names(self):
        if self.passangers!= []:
            print(f"Names of {self.brand}passangers: ")  
        for passanger in self.passangers:
            print(passanger.names)    
        else:
            print(f"There are no passangers in {self.brand}") 

nick = Human("Nick")
kate = Human("Kate")
max = Human("Max")
zahar = Human("Zahar")
car = Auto("Mercedes")
car1 = Auto("BMW")
cat = Animal("Cat")   
car.add_passanger(nick)
car.add_passanger(kate)  
car.add_passanger(max)        
car.add_passanger(zahar)
car.add_passanger(cat) 
print(car)
print(car1)


class Human:
    height = 170
class Child(Human):
    weight = 50
    pass
class Student(Child):
    pass

nick = Student()
ann = Student()
print(nick.weight)
print(ann.height)           

class Grandparent:
   height = 170
   satiety = 100
   age = 60
class Parent(Grandparent):
   age = 40
class Child(Parent):
 height = 50
 def init(self):
    print(self.height)
    print(self.satiety)
    print(self.age)
 
nick = Child()
   
class Hello_world:
    hello = "Hello"
    _hello = "_Hello"
    def init(self):
        self.world = "World"
        self._world = "_World"
    def printer(self):
        print(self.hello)
        print(self._hello)
        print(self.world)
        print(self._world)

class Hi(Hello_world):
    def hi_print(self):
        print(self.hello)
        print(self.world)
        print(self._hello)
        print(self._world)
    

hello = Hello_world()
hello.printer()
hi = Hi()
hi.hi_print()

class Computer:
    a = 10
def calculate(self):
    print("Calculating…")
class Display:
    a = 11
def display(self):
    print("I display the image on the screen…")

class SmartPhone(Display, Computer):
 pass

iphone = SmartPhone()
iphone.calculate()
iphone.display()

class Father:
    def FA(self):
      height = 180
class Son(Father):
    def SO(self):
      weight = 80
class Daughter(Son):
    def DA(self):
      fast = 50
class Daughterson(Daughter):
    def DASO(self):
      sprint = 200
class Mutant(Daughterson):
    def MU(self):
      crawl = 80

mutant = Mutant() 
print(mutant)   
                    