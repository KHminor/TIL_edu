import sys
from collections import deque
sys.stdin = open('sample_input (1).txt')
from pprint import pprint
T = int(input())
for tc in range(1,T+1):
    n,e = map(int,input().split())

    arr = [list(map(int,input().split())) for _ in range(e)]
    visited = [0]*(n+1)
    route = [[0]*(n+1) for _ in range(n+1)]

    for a in arr:
        route[a[0]][a[1]] = a[2]

    q = deque([0])
    while q:
        s = q.popleft()
        if s == n: continue
        for e in range(n+1):
            if route[s][e] != 0 and (not visited[e] or visited[e] > visited[s] + route[s][e]):
                visited[e] = visited[s] + route[s][e]
                q.append(e)
    print(f'#{tc} {visited[n]}')
