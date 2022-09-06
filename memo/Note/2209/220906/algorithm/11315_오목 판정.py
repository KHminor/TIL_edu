import sys
sys.stdin = open('sample_input (2).txt')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    col_arr = [['']*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            col_arr[i][j] = arr[j][i]

    # row
    result = ''
    cross = 0
    r_cross = 0
    for i in range(N):
        col = 0
        row = 0

        if arr[i][i] == 'o':
            cross += 1
        else:
            cross = 0
        if arr[i][N - 1 - i] == 'o':
            r_cross += 1
        else:
            r_cross = 0
        for j in range(N):
            if arr[i][j] == 'o':
                row += 1
            else:
                row = 0
            if col_arr[i][j] == 'o':
                col += 1
            else:
                col = 0
        if row >= 5:
            result = 'Yes'
            break
        elif col >= 5:
            result = 'Yes'
            break
        elif cross >= 5:
            result = 'Yes'
            break
        elif r_cross >= 5:
            result = 'Yes'
            break
    if result == '':
        result = 'NO'
    print(f'#{tc} {result}')