
class Employee:
    Company = 'Google'
    YearlySalary = 400000
    Yearbonus = 100000
    #If we need total salary to be dynamic, in this case it should be yearly sal + bonus; we uses getter i.e @property decorator

    @property
    def TotalSalary(self):
        return self.YearlySalary + self.Yearbonus
    
    @TotalSalary.setter
    def TotalSalary(self, TotalSalary):
        self.Yearbonus = TotalSalary - self.YearlySalary
        
e = Employee()
print (e.TotalSalary)

#setter to set Yearbonus

e.TotalSalary = 600000

print(e.Yearbonus)


