import random
import time

class Array:
    def __init__(self, length: int):
        self.arr = random.sample(range(1, length*2), length) 
        
class Sorting(Array):
    def __init__(self, length: int):
        super().__init__(length)

    def bubble_sort(self):
        for i in range(len(self.arr) - 1):
            flag = True
            for j in range(len(self.arr) - 1 - i):
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j],self.arr[j + 1] = self.arr[j + 1],self.arr[j]
                    flag = False
            if flag:
                break
        return self.arr
    
    def selection_sort(self):
        for i in range(len(self.arr) - 1):
            min_index = i
            for j in range(i + 1, len(self.arr)):
                if(self.arr[j] < self.arr[min_index]):
                    min_index = j
            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]
        return self.arr
    
    def merge_sort(self, arr=None):
        if arr is None:
            arr = self.arr

        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        self.merge_sort(left)
        self.merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        return arr

    
class Comparison(Sorting):
    def __init__(self, length):
        super().__init__(length)

    def sort_array(self, sort_func):
        start_time = time.time()
        result = sort_func()
        end_time = time.time()
        time_taken = "{:.6f}".format(end_time - start_time)
        return time_taken

    def compare(self, sort_func1, sort_func2):

        # Comparing 1st sort function
        self.arr1 = self.arr[:]
        result1 = self.sort_array(sort_func1)

        # Comparing 2st sort function
        self.arr = self.arr1[:]
        result2 = self.sort_array(sort_func2)

        return result1, result2


sorting_obj = Sorting(10)
print(sorting_obj.arr)   
print(sorting_obj.bubble_sort())  
print(sorting_obj.selection_sort())  
print(sorting_obj.merge_sort())

comparison_obj = Comparison(10000)
result_bubble, result_selection = comparison_obj.compare(comparison_obj.bubble_sort, comparison_obj.selection_sort)
result_bubble, result_merge = comparison_obj.compare(comparison_obj.selection_sort, comparison_obj.merge_sort)
print(result_bubble)
print(result_selection)
print(result_merge)
