<<<<<<< HEAD
from sys import stdin
read = stdin.readline
N,M,V = map(int,read().split)
a,b = map(int,read().split)

print(N,M,V,a,b)
=======
def dfs(v):
    stack = [v]
    visited = [0]*(N+1)
    while stack:
        v = stack.pop()
        if visited[v] == 0:
            print(v , end = ' ')
            visited[v] = 1

        arr[v].sort(reverse=True)
        for j in arr[v]:
            if visited[j] == 0:
                stack.append(j)


def bfs(v):
    visited = [0]*(N+1)
    q = [v]

    while q:
        v = q.pop(0)
        if visited[v] == 0:
            visited[v] = 1
            print(v, end = ' ')
        arr[v].sort()
        for j in arr[v]:
            if visited[j] == 0:
                q.append(j)

N,M,V = map(int,input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

dfs(V)
print()
bfs(V)
>>>>>>> ce22527a6c80400c63323737368d6e12a386d119
