num = int(input("Enter number : "))

for i in range(1, num+1):
    for j in range(i, num):
        print(" ", end="")
    for k in range(1, i+1):
        print("*", end="")
    print("\n")

#Other way

for i in range(1, num+1):
    print(" " * (num-i), end="")
    print("*" * (i))