import sys
sys.stdin = open('sample_input (1).txt')
T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())    # 연결지점 번호 N 도로 개수 E
    # [s, e, w] 구간 시작 s 끝 e 거리 w
    arr = [list(map(int, input().split())) for _ in range(E)]
    cnt = 0
    visited = [0] * (N + 1)
    route = [[0] * (N + 1) for _ in range(N + 1)]

    for a in arr:
        route[a[0]][a[1]] = a[2]

    q = [0]
    while q:

        s = q.pop()       # BFS (pop(0)) 도 가능

        for e in range(N + 1):
            if route[s][e] != 0 and (not visited[e] or visited[e] > visited[s] + route[s][e]):
                visited[e] = visited[s] + route[s][e]
                q.append(e)
                cnt += 1

    print(f'#{tc} {visited[N]}')
    print(cnt)
    print(route)