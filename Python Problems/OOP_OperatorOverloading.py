
class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        return self.num + num2.num
    
    def __mul__(self, num2):
        return self.num * num2.num
    
    # def __str__(self):
    #     return self.num
    
n1 = Number(4)
n2 = Number(2)  
sum = n1 + n2
print (sum)
mul = n1 * n2
print (mul)

# print (n1)