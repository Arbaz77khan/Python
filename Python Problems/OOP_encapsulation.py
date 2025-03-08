class Employee:

    '''Docstring : This class will have empno, name, salary, exp at attributes and their methods.
        Main purpose of this class is to give clear understanding of public,private and protected attributes/methods and learning on getter/setter methods'''
    
    def __init__(self, empno, name, salary):
        self.empno = empno  # This is public attribute and can be Accessible from anywhere, both inside and outside the class.
        self._name = name   # This is protected attribute denoted by '-' and can be Accessible within the class and its subclasses. 
        self.__salary = salary #This is private attribute denoted by '__' and Accessible only within the class

    # Adding getter here. It is used to see attributes
    @property   # by using this decorator we can simplify calling convention of attribute
    def get_salary(self):
        print (self.__salary)

    # Adding setter here. Its mainly used to update the value of private attribute which adding some layer of validation.
    @get_salary.setter
    def set_salary(self, new_value):
        if type(new_value) != int:          # here we have added validation layer before updating private attribute
            print("Invalid input error.")
        else:
            self.__salary = new_value

    # We can also code getter and setter without decorators.

    def get_name(self):
        print(self._name)        

    def set_name(self, new_name):
        self._name = new_name

e = Employee(1, 'Arbaz', 30000)

# print(e.__salary) -> this line will not work as salary is private 
e.get_salary # As we have added decorator we do not need to add brackets here.

e.__salary = 'hehehe' # this line will be of no use bcz, In python internally private attribute __xyx is converted to _classname__xyz. keep in mind that Python does not provide true "private" attributes as can still access private with _classname__xyz.

e.set_salary = 11

e.get_salary

print(e._name)
'''
While the single leading underscore indicates that an attribute is protected, it doesn't prevent access. It serves as a signal to other developers, indicating that the attribute is intended for internal use within the class or its subclasses.

It's crucial to understand that these conventions are not strict rules enforced by the Python interpreter. Developers can access attributes regardless of the naming conventions. The convention is more about communication and expectations within a development team.
'''

e.get_name() # here as we haven't used decorator, we need to include ()

e.set_name('Ali')

e.get_name()
