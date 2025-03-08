l = [1,2,3,4,5,6,7,8,9]

for i in l:
    print("Yes" + str(i))

print(type(i))


#In range format

for i in range(10, 0, -1):
    print(i)

for i in range(8):
    print(i)
    

for i in range(2, 11, 2):      #range(start, stop, step-size)
    print(i)

for i in range(8):
    print(i)
else:
    print("end")

for i in range(8):
    print(i)
    if i == 3:
        break
        
for i in range(8):
    if i == 3:
        continue
    print(i)