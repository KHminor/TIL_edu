import sys
sys.stdin = open('input.txt')

T = int(input())
#     우 하 좌 상  ==> dr 값을 통해서 방향을 변경 해주려고 함.
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for tc in range(1,T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    i, j, dr, cnt = 0, 0, 0, 1
    arr[i][j] = cnt
    cnt += 1

    while cnt <= N*N:
        ni, nj = i+di[dr], j+dj[dr]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            i, j = ni, nj
            arr[i][j] = cnt
            cnt += 1
        else:
            dr = (dr+1)% 4

    print(f'#{tc}')
    for li in arr:
        print(li)  # 아스타리스크 (*) 를 사용하면 감싸고 있는것을 한겹 없애주는 듯.