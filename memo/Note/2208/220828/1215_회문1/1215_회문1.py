import sys
sys.stdin = open('input.txt')
T = 10
for tc in range(1,T+1):
    N = 8
    # 회문 길이
    h = int(input())

    arr = [list(input()) for _ in range(8)]
    ln = N-h+1
    c = []
    r_c = []
    result = 0
    col_arr = [[0]*N for _ in range(N)]

    # 90도 돌린 버전
    for i in range(N):
        for j in range(N):
            col_arr[i][j] = arr[j][i]

    # 가로부터 체크
    for i in range(N):
        for j in range(ln):
            c = arr[i][j:j+h]
            r_c = c[::-1]
            if c == r_c:
                result += 1

        for j in range(ln):
            c = col_arr[i][j:j + h]
            r_c = c[::-1]
            if c == r_c:
                result += 1

    print(f'#{tc} {result}')



# pprint(col_arr)