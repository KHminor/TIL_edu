import sys
sys.stdin = open('input (1).txt')
T = 10
for _ in range(T):
    N = int(input())  # tc 번호
    M = 100
    arr = [list(map(int,input().split())) for x in range(M)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    c_sum = rc_sum  = x_sum = y_sum = max = c = 0
    for i in range(M):
        x_sum = 0
        y_sum = 0
        c += arr[i][i]
        for j in range(M):
            x_sum += arr[i][j]
            y_sum += arr[j][i]
            if i+j == M-1:
                rc_sum += arr[i][M-1-i]

            if x_sum > max:
                max = x_sum
            if y_sum > max:
                max = y_sum
            if c_sum > max:
                max = c_sum
                c_sum = 0
            if rc_sum > max:
                max = rc_sum
                rc_sum = 0
    print(f'#{N} {max}')