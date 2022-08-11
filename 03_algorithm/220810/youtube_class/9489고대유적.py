import sys
sys.stdin = open('input1 (1).txt')

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]


    li = [list([0]*N) for _ in range(M)]

    # print(f'c_li의 값 {c_li}')

    c_max = r_max = cnt = 0

    for i in range(M):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
                li[i][j] = cnt
                if li[i][j] > r_max:
                    r_max = li[i][j]
            elif arr[i][j] == 0:
                cnt = 0

    for i in range(M):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
                li[j][i] = cnt

                if li[j][i] > c_max:
                    c_max = li[j][i]
            elif arr[j][i] == 0:
                cnt = 0

    if r_max > c_max:
        print(f'#{tc} {r_max}')
    else:
        print(f'#{tc} {c_max}')