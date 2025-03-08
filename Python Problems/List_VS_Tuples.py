import time
import sys

L = list(range(10000000))
T = tuple(range(10000000))

print("Size of List : ", sys.getsizeof(L), "Bytes")
print("Size of Tuple : ", sys.getsizeof(T), "Bytes")

start = time.time()
for i in L:
    i*2
print("List time taken : {:.6f}".format(time.time() - start))


start = time.time()
for i in T:
    i*2
print("Tuple time taken : {:.6f}".format(time.time() - start))