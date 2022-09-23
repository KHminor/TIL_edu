import sys
sys.stdin = open('sample_input.txt')
def dfs(si,sj):
    global N,result
    visited[si][sj] = 1
    if visited[ei][ej] == 1:
        result = 1
        return

    else:
        for di,dj in [[-1,0],[1,0],[0,-1],[0,1]]:
            if 0<=si+di<N and 0<=sj+dj<N and not visited[si+di][sj+dj] and arr[si+di][sj+dj] != 1:
                dfs(si+di,sj+dj)


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    result = 0
    si = sj = ei = ej = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 3:
                ei,ej = i,j
            elif arr[i][j] == 2:
                si,sj = i,j
    dfs(si,sj)
    print(f'#{tc} {result}')
