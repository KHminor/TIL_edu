# def fibo(n):
#     if n < 2:
#         return n
#     else:
#         return fibo(n-1) + fibo(n-2)

memo = [-1]*101
memo[0] = 0
memo[1] = 1

def fibo(n):
    if memo[n] == -1:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]



for i in range(5):
    print(i, fibo(i))

