import sys
def fibo(x):
    if x == 0 or x == 1:
        li[x] += 1
        return x
    else:
        return fibo(x-1) + fibo(x-2)


T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    li = [0,0]
    fibo(n)
    print(*li)