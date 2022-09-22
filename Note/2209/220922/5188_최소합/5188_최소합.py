# dfs 사용해서 완전탐색 해볼까?
import sys

sys.stdin = open('sample_input (1).txt')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    i = j = 0
    way = N * 2 - 1
    a = sum(i for i in range(1, way + 1))
    min_sum = (N * N - 1) * 10
    s = 0
    stack = [[i, j, s]]


    while stack:
        i, j, s = stack.pop()
        s += arr[i][j]

        if i == N - 1 and j == N - 1 :
            if min_sum > s:
                min_sum = s
                if min_sum == a:
                    break
            else:
                continue
        if s >= min_sum:
            continue

        # 아래,우측
        for ei, ej in [[1, 0], [0, 1]]:
            if 0 <= i + ei < N and 0 <= j + ej < N:
                stack.append([i + ei, j + ej,s])

    print(f'#{tc} {min_sum}')
