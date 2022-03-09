def fib(n):
    if (n < 1):
        return -1
    elif n == 1:
        return 0
    elif (n >= 2 and n <= 3):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(10))
