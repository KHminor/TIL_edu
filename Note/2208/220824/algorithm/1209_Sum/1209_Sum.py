import sys
sys.stdin = open('input (1).txt')
T = 10
N = 100
for _ in range(T):
    tc = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    max = x = rx = 0

    for i in range(N):
        r = c = 0
        bbb = arr[i][N-1-i]
        x += arr[i][i]
        rx += arr[i][N - 1 - i]

        for j in range(N):
            r += arr[i][j]
            c += arr[j][i]

            if r > max:
                max = r
            elif c > max:
                max = c
            elif x > max:
                max = x
            elif rx > max:
                max = rx


    print(f'#{tc} {max}')
