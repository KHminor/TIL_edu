import sys
sys.stdin = open('input.txt')


def check():
    # 배열의 크기
    N = 9
    # 체크할 배열의 크기
    C = 3
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 1~9까지 모두 더한 값의 크기
    max = 45

    # 가로 세로 확인
    for i in range(N):
        raw = col = 0
        for j in range(N):
            raw += arr[i][j]
            col += arr[j][i]
        # 만약 각 행, 열 을 더한 결과가 45가 아닌 경우 return 0
        if raw != max:
            return 0
        elif col != max:
            return 0

    # 체크할 범위의 크기를 구하기
    for i in range(C):
        i *= 3
        for j in range(C):
            j *= 3
            box = 0
            for x in range(C):
                for y in range(C):
                    box += arr[i+x][j+y]
            if box != max:
                return 0

    return 1

T = int(input())
for tc in range(1, T+1):
    result = check()
    print(f'#{tc} {result}')