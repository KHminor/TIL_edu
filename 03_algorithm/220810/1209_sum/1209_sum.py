import  sys
sys.stdin = open('input.txt')
T = 10
for _ in range(T):
    N = int(input())  #
    M = 100
    arr = [list(map(int,input().split())) for x in range(M)]

    # 오른쪽,아래, 왼쪽, 위 방향으로 가기위한 리스트
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

# 대각선의 합, 역 대각선의 합, x축 합, y축의 합, 최고값을 초기화
    c_sum = rc_sum  = x_sum = y_sum = max = 0
    for i in range(M):

        x_sum = 0 # x 축 한번 하고 초기화 해야 다음 줄을 더할때 영향이 가지 않기에 초기화
        y_sum = 0 # y 축 또한 한번 하고 초기화 해야 다음 줄을 더할때 영향이 가지 않기에 초기화
        c_sum += arr[i][i] # 대각선 방향 값 저장
        for j in range(M):
            x_sum += arr[i][j] # x축 방향 값 저장
            y_sum += arr[j][i] # y축 방향 값 저장
            if i+j == M-1:
                rc_sum += arr[i][M-1-i] # 역 대각선 방향 값 저장

            # 최고값 비교
            if x_sum > max:
                max = x_sum
            if y_sum > max:
                max = y_sum
            if c_sum > max:
                max = c_sum
                c_sum = 0
            if rc_sum > max:
                max = rc_sum
                rc_sum = 0
    print(f'#{N} {max}')

