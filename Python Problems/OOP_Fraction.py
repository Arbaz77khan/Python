class Fraction:
    # initalizing constructor here
    def __init__(self, x, y):
        self.num = x
        self.den = y

    def __str__(self):
        return '{}/{}'.format(self.num, self.den)
        
    # '+' operation method here
    def __add__(self, other):
        new_num = (self.num * other.den) + (self.den * other.num)
        new_den = (self.den * other.den)

        return '{}/{}'.format(new_num, new_den)



# Fraction objects
a = Fraction(3, 4)
b = Fraction(5, 6)

# int variables (But as we know In python all things are called as objects, c and d are also objects of class 'int' and if we write 'c.' we can get all methods of 'int' class)
c = 3
d = 5

# Types of both
print(type(a))
print(type(c))

# Because of __str__ method in class 'Fraction and Int',we are able to print a and c
print(a)
print(c)

# Add operation
print(a+b)
print(c+d)

