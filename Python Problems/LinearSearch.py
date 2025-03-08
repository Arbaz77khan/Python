def Linear_search(arr, item):
    for i in arr:
        if i == item:
            return True
    return False

result = Linear_search([1, 2, 3, 4], 3)

print(result)
