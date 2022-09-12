import sys
sys.stdin = open('input.txt')
# 우 하 좌 상
T = int(input())
for tc in range(1,T+1):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    max = N*N+1
    i = j = d = 0
    num = 1
    while num != max:
        arr[i][j] = num
        num += 1
        if 0 <= i+di[d] < N and 0 <= j+dj[d] < N and not arr[i+di[d]][j+dj[d]]:
            i,j = i+di[d], j+dj[d]

        else:
            d = (d+1)%4
            i, j = i + di[d], j + dj[d]
    print(f'#{tc}')
    for i in arr:
        print(*i)