num = int(input("Enter number : "))
flag = False
for i in range(2, num):
    if(num%i == 0):
        print(num, "is not a prime number")
        flag = True
        break

if not(flag):
        print(num, "is a prime number") 