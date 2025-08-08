def factorial(n):
    
    res = 1
    
    while n > 0:
        res *= n
        n -= 1
    
    return res

print(factorial(0))

print(factorial(1))

print(factorial(2))

print(factorial(3))

print(factorial(4))

print(factorial(5))