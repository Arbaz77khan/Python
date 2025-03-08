var1 = int(input("Enter number for multiplicaton table : "))

for i in range(1, 11):
    print(str(var1) + " X " + str(i) + " = " + str(var1*i))


# We can also perform print line by f string

for i in range(1, 11):
    #print(str(var1) + " X " + str(i) + " = " + str(var1*i))
    print(f"{var1} X {i} = {var1*i}")