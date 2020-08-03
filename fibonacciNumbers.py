def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        t = a
        a = b
        b = t + b


for i in fib(20):
  print(i)
