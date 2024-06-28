#blueprint of class
class Vehicle:
    #class variable or attributes or properties
    color = "red"
    no_of_tyres = 4
    seating_capacity = 5

    #class methods or functions or
    def start_the_engine(self):
        print("vehicle started")
    def press_the_break(self):
        print("vehicel stopped")

# creating an instance of blueprint/class that is object

My_car = Vehicle()
print(My_car)
print(My_car.color)
print(My_car.no_of_tyres)
My_car.start_the_engine()
My_car.press_the_break()





