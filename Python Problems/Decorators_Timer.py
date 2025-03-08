import time

def timer(func):
    def wrapper(*args):
        start = time.time()
        output = func(*args)
        print("Time taken by ", func.__name__, "is ", time.time() - start, "secs")
        return output
    return wrapper


@timer
def addition(a, b):
    result = 0
    for i in range(a, b + 1):
        result = result + i
    return result

@timer
def multiplication(a, b):
    result = 1
    for i in range(a, b + 1):
        result = result * i
    return result

Add = addition(99, 100)
mul = multiplication(99, 100)
print(Add)
print(mul)