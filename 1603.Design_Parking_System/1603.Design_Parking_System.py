#--------------LEET CODE---------------
#1603.Design Parking System

#Solution of Matvey Guralskiy
#https://github.com/MatveyGuralskiy 
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.slots = [0, big, medium, small]

    def addCar(self, car_type: int) -> bool:
        self.slots[car_type] = count = max(self.slots[car_type] - 1, -1)
        return count > -1