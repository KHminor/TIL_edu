from collections import deque
from pprint import pprint

def bfs():
    si,sj,ei,ej = 0,0,n-1,n-1
    cnt = 0
    q = [[si,sj]]
    visited = [[1000000]*n for _ in range(n)]
    visited[si][sj] = 0
    while q:
        si,sj = q.pop(0)
        visited[si][sj] = 1
        if (si,sj) == (ei,ej):
            break

        else:
            for di,dj in [[-1,0],[1,0],[0,-1],[0,1]]:
                if 0<=si+di<n and 0<=sj+dj<n:
                    if arr[si+di][sj+dj] - arr[si][sj] >= 0:
                        if visited[si+di][sj+dj] > visited[si+di][sj+dj] + arr[si+di][sj+dj] - arr[si][sj] +1 :
                            visited[si+di][sj+dj] = visited[si+di][sj+dj] + arr[si+di][sj+dj] - arr[si][sj] +1
                            q.append([si+di,sj+dj])
                    else:
                        if visited[si+di][sj+dj] > visited[si][sj] + 1:
                            visited[si+di][sj+dj] = visited[si][sj] + 1
                            q.append([si+di,sj+dj])

                        # T = int(input())
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
bfs()
print(visited)