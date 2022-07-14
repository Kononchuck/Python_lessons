fib_num = lambda n: fib_num(n-1) + fib_num(n-2) if n > 2 else 1

print(fib_num(8))