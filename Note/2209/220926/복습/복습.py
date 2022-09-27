# 순열(재귀)
def nPr(s,n):
    if s == n:
        print(a)
    else:
        for i in range(s,n):
            a[s],a[i] = a[i],a[s]
            nPr(s+1,n)
            a[s],a[i] = a[i],a[s]

def nPr1(s,n):
    if s == n:
        print(a)
    else:
        for i in range(n):
            if not visited[i]:
                p[s] = a[i]
                nPr(s+1,n)

def nCr(s,n,k):
    if k == 0:
        print(p)
    else:
        for i in range(s,n-k+1):
            p[k-1] = p[i]
            nCr(i+1,n,k)

n = 5
k = 3
visited = [0]*(n+1)
p = [0]*(n+1)
a = [i for i in range(1,n+1)]
# nPr(0,n)
nCr(0,n,k)
