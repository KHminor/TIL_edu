# 재귀를 활용한 조합 만들기

def nCr(s,n,r):
    if r == 0:
        print(*sorted(p))

    else:
        for i in range(s,n-r+1):
            p[r-1] = a[i]
            nCr(i+1,n,r-1)

n = 6
r = 3
a = [i for i in range(1,n+1)]
p = [0]*r
nCr(1,n,r)