def per(n):
    if True: a = 12
    else:
        return n * per(n-1)

n = int(input())
per(n)