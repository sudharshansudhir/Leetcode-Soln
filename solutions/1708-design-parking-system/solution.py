class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.slot=[big,medium,small]

    def addCar(self, carType: int) -> bool:
        flag=True
        if carType==1:
            if self.slot[0]>0:
                self.slot[0]-=1
                return True
            else:
                return False
        elif carType==2:
            if self.slot[1]>0:
                self.slot[1]-=1
                return True
            else:
                return False
        elif carType==3:
            if self.slot[2]>0:
                self.slot[2]-=1
                return True
            else:
                return False
        
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
