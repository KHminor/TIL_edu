import sys
sys.stdin = open('sample_input (1).txt')
from collections import deque
T = int(input())
for tc in range(1,T+1):
    n,e = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(e)]
    w_arr = [[0]*(n+1) for _ in range(n+1)]
    visited = [0]*(n+1)

    for a in arr:
        w_arr[a[0]][a[1]] = a[2]

    q = deque([0])
    while q:
        s = q.popleft()

        for e in range(n+1):
            if w_arr[s][e] != 0 and (not visited[e] or visited[e] > visited[s]+ w_arr[s][e]):
                visited[e] = visited[s] + w_arr[s][e]
                q.append(e)

    print(f'#{tc} {visited[-1]}')

