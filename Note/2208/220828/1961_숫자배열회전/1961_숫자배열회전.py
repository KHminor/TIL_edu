import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    # 배열의 크기
    N = int(input())
    # 같은 크기의 2차원 배열
    arr = [list(map(int,input().split())) for _ in range(N)]
    s = ''
    for i in range(N):
        for j in range(N):
            # one_li
            s += str(arr[N-1-j][i])
        s += ' '
        for j in range(N):
            # two_li
            s += str(arr[N-1-i][N-1-j])
        s += ' '
        for j in range(N):
            # three_li
            s += str(arr[j][N-1-i])
        s += '\n'
    print(f'#{tc}')
    print(s, end='')