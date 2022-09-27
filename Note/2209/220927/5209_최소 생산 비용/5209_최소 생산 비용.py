import sys
sys.stdin = open('sample_input (5).txt')
def factory(i,s):
    global result
    if i == n:
        if result > s:
            result = s
            return
        else:
            return
    else:
        if s >= result:
            return
        else:
            for j in range(n):
                if not visited[j]:
                    visited[j] = 1
                    s += arr[i][j]
                    factory(i+1,s)
                    visited[j] = 0
                    s -= arr[i][j]
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    visited = [0]*n
    s = 0
    result = 99*n
    factory(0,s)
    print(f'#{tc} {result}')