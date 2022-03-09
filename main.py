def fib(n):
    
    prev, cur = 0, 1
    
    print(prev)
    for i in range(0, n - 1):
        prev, cur = cur, prev + cur
        print(prev)

fib(10)
