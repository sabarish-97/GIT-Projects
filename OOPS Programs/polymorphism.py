class vehicle:
    def __init__(self, colour, weight, maxspeed):
        self.colour = colour
        self.weight = weight
        self.maxspeed = maxspeed

    def move(self, speed):
        print(f"car is moving in {speed} km/hr")    

class Car(vehicle):
    def __init__(self, colour, weight, maxspeed, form_factor):
        super().__init__(colour, weight, maxspeed)
        self.form_factor = form_factor

    def move(self, speed):
        print(f"car is moving in {speed} km/hr")

class Animal:
    def move1(self):
        print(f"tiger moves in {self.maxspeed} in km/hr")


generic_vehicle = vehicle("blue", 4000, 400)  
generic_vehicle.move(150)     

car = Car("red", 2000, 300, "suv")  
car.move(500)

animal = Animal()
animal.move1(20009)