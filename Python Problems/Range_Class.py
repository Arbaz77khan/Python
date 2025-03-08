import sys
l1 = [i for i in range(10000)]

print("L1:", sys.getsizeof(l1), "Bytes")
print("L1:", sys.getsizeof(l1)/1024, "KB")
print("L1:", sys.getsizeof(l1)/1024**2, "MB")

l2 = range(10000)

print("L1:", sys.getsizeof(l2), "Bytes")
print("L1:", sys.getsizeof(l2)/1024, "KB")
print("L1:", sys.getsizeof(l2)/1024**2, "MB")

print(type(l1))

print(type(l2))

'''
You'll likely observe that the size of the list (l1) is significantly larger than the size of the range object (l2). This is because a range object represents a sequence of numbers in a compact form without explicitly storing each individual element, whereas a list stores each element separately, leading to higher memory usage.
'''

# for i in l1:
#     print(i, end=",")

# for i in l2:
#     print(i, end=",")


'''
The key point here is that a range object in Python is more memory-efficient than a list, especially when dealing with large sequences of numbers.
'''

# List, tuple is an iterable
# range is an iterator

# print(dir(l1))
iter_list = iter(l1)

next(iter_list)


