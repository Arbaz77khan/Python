
class College:                                  # Parent class
    collageName = 'Modern college'

    def admission(self):
        print("Admission Done !!!")

class Student(College):                         #Child class
    
    def course(self):
        print("Course taken !!!")


c1 = College()
s1 = Student()

print(c1.collageName)
print(s1.collageName)                           # -> child class can also access attributes and methods of parent class.                  

s1.admission()