def fact_iter(num):
    sum = 1
    for i in range(1, num+1):
        sum = sum * i 
    return(sum)  


def fact_recursion(num):
    if num == 0 or num == 1:
        return 1
    else:
        return(num*fact_recursion(num-1))

factorial =  fact_iter(4)   

factorial1 =  fact_recursion(4)  

print(factorial)

print(factorial1)