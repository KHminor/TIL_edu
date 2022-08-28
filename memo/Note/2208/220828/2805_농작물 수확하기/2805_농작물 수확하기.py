import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]

    moc = N//2
    sum = 0
    # 반복 횟수
    z = 1
    x = moc
    for i in range(N):
        j = i
        for _ in range(z):
            sum += arr[i][x-j]
            j  -= 1
            # 상단
        if i < moc:
            z += 2
        elif i >= moc:
            z -= 2
            x += 2

    print(f'#{tc} {sum}')