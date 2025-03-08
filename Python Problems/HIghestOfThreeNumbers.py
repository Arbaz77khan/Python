def highest(num1,num2,num3):
    if (num1 > num2):
        if (num1 > num3):
            return num1
        else:
            return num3
    else:
        if (num2 > num3):
            return num2  
        else:
            return num3

num1 = int(input("Enter num 1 : "))
num2 = int(input("Enter num 2 : "))
num3 = int(input("Enter num 3 : "))

print("Highest is : ",highest(num1,num2,num3))

