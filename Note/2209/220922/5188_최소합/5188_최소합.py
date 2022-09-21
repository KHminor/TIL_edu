# dfs 사용해서 완전탐색 해볼까?
import sys
sys.stdin = open('sample_input (1).txt')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    i = j = cnt = 0
    way = N*2-1
    a = sum(i for i in range(1,way+1))
    min_sum = (N*N-1)*10
    s = 0
    stack = [[i,j,cnt,s]]

    while stack:
        i,j,cnt,s = stack.pop(0)
        s += arr[i][j]
        if i == N-1 and j == N-1 and cnt == way-1:
            if min_sum > s:
                min_sum = s
                if min_sum == a:
                    break
            else:
                continue

        else:
            # 아래,우측
            for ei,ej in [[1,0],[0,1]]:
                if 0 <= i+ei <N and 0 <= j+ej <N:
                    c_cnt = cnt
                    stack.append([i+ei,j+ej, c_cnt+1,s])

    print(f'#{tc} {min_sum}')
