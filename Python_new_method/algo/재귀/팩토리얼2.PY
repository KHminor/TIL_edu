def fectorial(n):
    if 1>=n: return 1
    return n*fectorial(n-1)
print(fectorial(int(input())))


def fectorial(n):
    if li[n]: return li[n]
    li[n] = n*fectorial(n-1)
    return li[n]

n = int(input())
li = [0]*(n+1)
li[0] = 1
fectorial(n)
print(li[n])