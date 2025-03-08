
class Programmers:
    company = 'Microsoft'
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getInfo(self):
        print(f"Company : {self.company} -> Employee name is {self.name} and salary is {self.salary}")

emp1 = Programmers('Arbaz', 400000)

emp2 = Programmers('Raj', 350000)

emp1.getInfo()
emp2.getInfo()