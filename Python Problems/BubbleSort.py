def bubbleSort(arr):
    for i in range(len(arr)-1):
        flag = True
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                flag = False
            print(arr)
        if flag:
            break
    print(arr)

arr = [1, 2, 3, 4, 5]
bubbleSort(arr)