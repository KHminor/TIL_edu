def fibo(n):
    f = [0, 1]
    for i in range(2, n+1):
        f.append(fibo(i-2)+fibo(i-1))
    return f[n]
print(fibo(3))
