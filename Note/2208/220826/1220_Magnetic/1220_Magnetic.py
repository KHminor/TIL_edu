import sys
sys.stdin = open('input (3).txt')
from pprint import pprint
# 1: N극 아래로 , 2: S극 위로
T = 10
for tc in range(1, T+1):
    N = int(input())
    arr =  [list(map(int,input().split())) for _ in range(N)]
    # N 극은 아래로 내려가는데 조사 또한 내려가며 조사하기에
    # 계속 이동할 수 있으므로 방문조사 체크
    visited = [[0]*N for _ in range(N)]

    # 아래, 위
    di = [1, -1]
    # dj = [0, 0]

    while True:
        deadlock = cnt = 0
        for i in range(N):
            for j in range(N):
                # N극의 경우 그리고 아래로 이동 가능한 범위의 경우
                if arr[i][j] == 1 and 0 <= i+di[0] < N and visited[i+di[0]][j] != 1:
                    # 현재 위치가 배열의 가장 마지막일때 현재 위치를 0으로 비우기
                    if i == N-1:
                        arr[i][j] = 0
                        # 아직 이동 중인것을 체크 후 반복문 탈출
                        cnt += 1
                        break
                    # 현재 위치에서 아래로 내려갈때
                    else:
                        # 이동할 곳인 아래가 0일 경우
                        if arr[i+di[0]][j] == 0:
                            # 이동할 다음 곳을 우선 방문했다는 것으로 다시 연산 X
                            visited[i+di[0]][j] = 1
                            # 현재 위치인 1의 값과 다음 이동할 위치 0 의 값을 서로 바꾸기
                            arr[i][j],arr[i+di[0]][j] = 0, 1
                            # 더이상 움직이지 않는 것을 체크하기 위해
                            cnt += 1
                        # 아래가 2인 S극의 경우는
                        elif arr[i+di[0]][j] == 2:
                            # 교착 상태 체크
                            deadlock += 1

                # S극의 경우엔 위로 올라가기에 다시 연산 되지 않아서 visited 사용 X
                elif arr[i][j] == 2 and 0 <= i+di[1] < N:
                    # 현재 위치가 배열의 가장 위일때 현재 위치를 0으로 비우기
                    if i == 0:
                        arr[i][j] = 0
                        # 아직 이동중인 것을 체크
                        cnt += 1
                        break
                    # 현재 위치에서 위로 올라갈때
                    else:
                        # 이동할 곳인 위가 0일 경우
                        if arr[i+di[1]][j] == 0:
                            # 현재 위치인 1의 값과 다음 이동할 위치 0 의 값을 서로 바꾸기
                            arr[i][j],arr[i+di[1]][j] = 0, 2
                            # 더이상 움직이지 않는 것을 체크하기 위해
                            cnt += 1
        if cnt == 0:
            break
    print(f'#{tc} {deadlock}')