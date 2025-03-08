num = int(input("Enter number : "))

for i in range(1, num+1):
    print(" " * (num-i), end="")
    print("*" * (i*2-1))