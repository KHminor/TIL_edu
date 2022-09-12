import sys
sys.stdin = open('input (1).txt')
from pprint import pprint
T = int(input())
for tc in range(1, T+1):
    N,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        sum = 0
        for j in range(N):
            if arr[i][j] == 1:
                sum += 1
            elif arr[i][j] == 0:
                if sum == K:
                    result += 1
                    sum = 0
                else:
                    sum = 0
            # if sum > K:
            #     break
        if sum == K:
            result += 1
    # print(result)


    # 90도 돌린 2차원 배열
    col_arr = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            col_arr[i][j] = arr[j][i]

    for i in range(N):
        sum = 0
        for j in range(N):
            if col_arr[i][j] == 1:
                sum += 1
            elif col_arr[i][j] == 0:
                if sum == K:
                    result += 1
                    sum = 0
                else:
                    sum = 0
            # if sum > K:
            #     break
        if sum == K:
            result += 1
    print(f'#{tc} {result}')
# pprint(col_arr)

