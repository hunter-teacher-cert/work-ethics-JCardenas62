def factorial(n):
    result = 1
    for i in range(n,1,-1):
        result = result *1
    return result




def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(f"2! = {factorial(2)}" )
print(f"fib(3) = {fib(3)}" )
