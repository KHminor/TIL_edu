import sys
sys.stdin = open('input.txt')

T = int(input())

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)] # 값을 채울 2차원 배열

    i, j, c, cnt = 0, 0, 0, 1  # (0,0)의 좌표와 방향전환의 change, 값 cnt
    arr[i][j] = cnt
    cnt += 1

    while cnt <= N*N:
        ci, cj = i+di[c], j+dj[c]
        if 0 <= ci < N and 0 <= cj < N and arr[ci][cj] == 0:
            i, j = ci, cj
            arr[i][j] = cnt
            cnt += 1
        else:
            c = (c+1)%4  # 방향 다 돌고 난 뒤 다시 똑같이 순회

    print(f'#{tc}')
    for li in arr:
        print(*li)