import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):

    N, M, V = map(int, input().split())
    arr = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    # print(ch1)

    # dfs 우선 - stack 사용
    visited = [0]*(N+1)
    ch1[v1].sort(reverse=True)
    stack = ch1[v1]
    visited[v1] = 1
    result = [v1]
    num = []
    while stack:
        v1 = stack.pop()
        if visited[v1] == 0:
            result.append(v1)
            for i in range(len(ch1[v1])):
                if ch1[v1][i] != 0 :
                    num.append(ch1[v1][i])
                    num.sort(reverse=True)
            for j in num:
                stack.append(j)
        visited[v1] = 1
    print(*result)

    # bfs - q 사용
    visited = [0]*(N+1)
    ch2[v2].sort()
    q = ch2[v2]
    visited[v2] = 1
    result2 = [v2]
    num = []
    while q:
        v2 = q.pop(0)
        if visited[v2] == 0:
            result2.append(v2)
            for i in range(len(ch2[v2])):
                if ch2[v2][i] != 0 :
                    num.append(ch2[v2][i])
                    num.sort()
            for j in num:
                q.append(j)
        visited[v2] = 1
    print(*result2)

