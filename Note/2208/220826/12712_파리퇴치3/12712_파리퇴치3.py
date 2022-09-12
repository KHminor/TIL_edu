from pprint import pprint
import sys
sys.stdin = open('in1.txt')
T = int(input())
for tc in range(1, T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # + 방향으로의 합계를 담는 arr
    ch_arr = [[0]*N for _ in range(N)]
    # x 방향으로의 합계를 담는 arr
    cross_arr = [[0]*N for _ in range(N)]
    # 상하좌우
    pi = [-1, 1, 0, 0]
    pj = [0, 0, -1, 1]
    # 상좌 상우 하우 하좌
    ci = [-1, -1, 1, 1]
    cj = [-1, 1, 1, -1]
    # 가장 최대의 크기를 담는 변수
    max = 0
    for i in range(N):
        for j in range(N):
            # +, x 의 범위를 더하는 변수 초기화
            plus = cross = 0
            # plus, cross 모두 현재 좌표의 값을 우선 더한 후 진행
            plus += arr[i][j]
            cross += arr[i][j]
            # 델타탐색으로 해당 좌표로 이동 가능한지 확인 후 가능할 경우 이동후 해당 좌표 값 더하기
            for d in range(4):
                # 상하좌우
                for gob in range(1,M):
                    if 0 <= i + (pi[d]*gob) < N and 0 <= j + (pj[d]*gob) < N:
                        plus += arr[i+(pi[d]*gob)][j+(pj[d]*gob)]
                # 상좌 상우 하우 하좌
                for gob in range(1,M):
                    if 0 <= i + (ci[d]*gob) < N and 0 <= j + (cj[d]*gob) < N:
                        cross += arr[i+(ci[d]*gob)][j+(cj[d]*gob)]
            # 방향별로 더한 값중 큰 값을 max에 넣기
            if plus > max:
                max = plus
            if cross > max:
                max = cross
            # 아래 코드는 그냥 확인하고 싶어서 따로 저장
            cross_arr[i][j] = cross
            ch_arr[i][j] = plus

    print(f'#{tc} {max}')
