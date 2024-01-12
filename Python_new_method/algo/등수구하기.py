import sys
input = sys.stdin.readline

n,n_score,p = map(int,input().split())

if n == 0: print(1)
else:
    li = list(map(int,input().split()))
    if n == p and li[-1] >= n_score: print(-1)
    else: 
        result = n+1
        for i in range(n):
            if n_score >= li[i]: 
                result = i+1
                break
        print(result)