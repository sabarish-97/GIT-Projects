class vehicle:
    def __init__(self, colour, speed , size):
        self.colour = colour
        self.speed = speed
        self.size = size

    def car(self):
        print(f"this vehicle is {self.colour} in {self.size} m moves in {self.speed}")



def user_input():
    
    global max_speed
    max_speed = input(str("pleasae type maximum speed"))
    global color1
    color1 = input(str("colour?"))
    global size1
    size1 = input(str("size?"))
    
    
user_input()
vehicle_object = vehicle(color1, max_speed, size1)
vehicle_object.car()