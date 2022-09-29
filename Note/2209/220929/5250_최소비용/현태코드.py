
from collections import deque


# 지역의 높이에 따라 연료 소비량이 달라진다.
# 출발은 맨 왼쪽 위, 도착은 가장 오른쪽 아래
# 기본적으로 인접 지역 -> 1소비 , 높이 차이만큼 + 소비

def bfs(n):
    q = deque()
    q.append(n)
    while q:
        sti, stj = q.popleft()
        di, dj = [1,-1,0,0],[0,0,1,-1]
        for i in range(4):
            ni, nj = di[i]+sti, dj[i]+stj
            if 0<=ni < N and  0<=nj < N:
                if arr[ni][nj] - arr[sti][stj] >= 0:
                    if visited[ni][nj] > visited[sti][stj] + arr[ni][nj] - arr[sti][stj] + 1:
                        visited[ni][nj] = visited[sti][stj] + arr[ni][nj] - arr[sti][stj] + 1
                        q.append([ni, nj])
                else:
                    if visited[ni][nj] > visited[sti][stj] + 1:
                        visited[ni][nj] = visited[sti][stj] + 1
                        q.append([ni, nj])
                # visited[ni][nj] = min(visited[sti][stj]+abs(arr[sti][stj] - arr[ni][nj])+1, visited[ni][nj])
                # q.append([ni, nj])


    return visited

# T = int(input())
# for tc in range(1, T+1):
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[1000000] * N for _ in range(N)]
visited[0][0] = 0
bfs((0,0))
print(visited)