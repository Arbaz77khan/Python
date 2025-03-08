
num = input("Enter the number : ")

try:
    print("program is running")
    if (num > 10):
        print("Number is greater than 10")
    else:
        print("Number is less than 10")   
except Exception as e:
    print(f"Error{e}")
print("program ends here")