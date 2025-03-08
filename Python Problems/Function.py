def greeting():
    print("Good Morning!!! ")

def greeting1(name="Arbaz"):
    print("Good Morning!!! ",name)

def percent(marks):
    ans = (sum(marks)*100)/500
    return(ans)

stud1 = [67,98,76,56,88]
stud2 = [87,98,99,76,56]

greeting()

greeting1()   #Will take default value is any argument is not passed

greeting1("Salman")

percentage1 = percent(stud1)

percentage2 = percent(stud2)

print(percentage1,percentage2)
