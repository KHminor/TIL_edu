import sys
sys.stdin = open('input1.txt')
T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ch_li = [[0]*M for _ in range(N)]
    col_li = [[0]*N for _ in range(M)]
    ch_col = [[0]*N for _ in range(M)]
    max = 0

    for a in range(N):
        for b in range(M):
            col_li[b][a] = arr[a][b]

    # print(arr)
    # print(col_li)

    # 정 사각형이 아닐 수 있기에
    # 우선 가로부터 체크
    for i in range(N):
        cnt = 0
        for j in range(M):
            if arr[i][j]:
                cnt += 1
                ch_li[i][j] = cnt
                if cnt > max:
                    max = cnt
            else:
                cnt = 0
                ch_li[i][j] = cnt

    for i in range(M):
        cnt = 0
        for j in range(N):
            if col_li[i][j]:
                cnt += 1
                ch_col[i][j] = cnt
                if cnt > max:
                    max = cnt
            else:
                cnt = 0
                ch_col[i][j] = cnt
    #
    # print(ch_li)
    # print(ch_col)
    print(f'#{tc} {max}')