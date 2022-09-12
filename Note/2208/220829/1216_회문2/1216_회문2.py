import sys
sys.stdin = open('input (1).txt')
T = 10
for _ in range(T):
    tc = int(input())
    N = 100
    arr = [list(input()) for _ in range(N)]
    max = 0
    col_arr = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            col_arr[i][j] = arr[j][i]

    for i in range(N):
        for j in range(N):
            for x in range(j+1,N+1):
                ch_li = arr[i][j:x]
                col_ch_li = col_arr[i][j:x]
                if arr[i][j:x] == ch_li[::-1] and len(ch_li) > max:
                    max = len(ch_li)
                if col_arr[i][j:x] == col_ch_li[::-1] and len(col_ch_li) > max:
                    max = len(col_ch_li)

    print(f'#{tc} {max}')