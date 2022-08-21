def fibo(x):
    if x == 1:
        return 1
    elif x == 0:
        return 0
    else:
        return fibo(x-1) + fibo(x-2)

N = 6
print(fibo(N))