from collections import deque
import sys
sys.stdin = open('sample_input.txt')
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    visited = [[100000]*n for _ in range(n)]
    visited[0][0] = 0
    q = deque([[0,0]])
    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    cnt =0
    while q:
        i,j = q.popleft()
        if visited[i][j] > visited[n-1][n-1]: continue
        for x in range(4):
            ni,nj = i+di[x], j+dj[x]
            # 다음 방문 좌표가 나보다 큰 경우만 조사
            if 0<=ni<n and 0<=nj<n:
                if arr[ni][nj] >= arr[i][j]:
                    a = visited[i][j]+(arr[ni][nj]-arr[i][j])+1
                else:
                    a = visited[i][j]+1
                if visited[ni][nj] > a:
                    visited[ni][nj] = a
                    q.append([ni,nj])
                    cnt+=1
    print(cnt)
    print(f'#{tc} {visited[n-1][n-1]}')