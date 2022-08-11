import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):
    M = int(input())

    arr = [list(map(int,input().split())) for _ in range(M)]
    sum = 0
    di = [0, 0, -1, 1] # 상하좌우
    dj = [-1, 1, 0, 0]
    for i in range(M):
        for j in range(M):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < M and 0 <= nj < M: # 유효한 인덱스면
                    minus = arr[i][j] - arr[ni][nj]
                    if minus < 0:
                        Ab = (minus)*-1
                        sum += Ab
                    else:
                        sum += minus
    print(f'#{tc} {sum}')