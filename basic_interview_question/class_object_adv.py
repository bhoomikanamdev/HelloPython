#blueprint of class
class Vehicle:
    #class variable or attributes or properties
    color = "red"
    no_of_tyres = 4
    seating_capacity = 5

    #constructor - always called and always will be called first
    def __init__ (self,color,no_of_tyres,seating_capacity):
        #self will hold entire object including properties and methods
        print("this is constructor" ,self.color)
        self.color = color
        self.no_of_tyres = no_of_tyres
        self.seating_capacity = seating_capacity

    #class methods or functions or
    def start_the_engine(self):
        print("vehicle started")
    def press_the_break(self):
        print("vehicel stopped")

# creating an instance of blueprint/class that is object

'''My_car = Vehicle()
print(My_car)
print(My_car.color)
print(My_car.no_of_tyres)
My_car.start_the_engine()
My_car.press_the_break()'''

My_bus = Vehicle('green',6 , 20)
print(My_bus.color)
print(My_bus.no_of_tyres)
print(My_bus.seating_capacity)
My_bus.start_the_engine()
My_bus.press_the_break()







