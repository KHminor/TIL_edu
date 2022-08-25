# 우선 아래의 방향이 있다면 먼저 내려가고
# 아래로 내려가다가 좌우 방향이 있다면 해당 방향으로
# 델타 탐색을 이용하여 움직여서 최종 방향인 2를 찾으면
# 출발한 j의 값을 리턴 하면 될 것 같다.
T = 10
N = 100
tc = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
# 아래 좌 우
di = [1, 0, 0]
dj = [0, -1, 1]

i = j = 0
while True:
    if arr[i][j] == 1:
        if arr[i+di[0]][j] == 1:        # 아래의 방향이 1로 지나갈 수 있는 경로의 경우
