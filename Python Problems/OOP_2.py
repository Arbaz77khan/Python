
class Calculator:
    def __init__(self,num):
        self.number = num

    def calSquare(self):
        print(f"The square of {self.number} is {self.number **2}")

    def calCube(self):
        print(f"The cube of {self.number} is {self.number **3}")
    
    def calSquareroot(self):
        print(f"The square root of {self.number} is {self.number **0.5}")

num = Calculator(2)

num.calSquare()

num.calCube()

num.calSquareroot()