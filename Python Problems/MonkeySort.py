import random

def isSorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

def monkeySort(arr):
    while not isSorted(arr):
        random.shuffle(arr)
    print(arr)


arr = [12, 3, 4, 5, -1, 10]

monkeySort(arr)