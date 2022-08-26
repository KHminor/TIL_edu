import sys
sys.stdin = open('input (1).txt')
from pprint import pprint
T = 10
for _ in range(T):
    tc = int(input())
    N = 100
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    # 도착 지점으로부터 출발지점을 찾기

    # 우선 도착지점을 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                ei,ej = i,j
                break

    # 스택 초기화
    stack = []

    # 출발지에 도착했을 경우 열의 값을 담기 위한 변수
    result = 0

    while True:
        # 현재 좌표를 방문했음을 체크
        visited[ei][ej] = 1

        # 만약 현재 좌표의 행의 값이 0의 경우 출발지점이기에 열의 값을 담고 탈출
        if ei == 0:
            result = ej
            break

        # 좌 우 상
        for i,j in [[0, -1], [0, 1], [-1, 0]]:
            if 0 <= ei+i < N and 0 <= ej+j < N and arr[ei+i][ej+j] != 0 and not visited[ei+i][ej+j]:
                ei, ej = ei+i, ej+j
                break

    print(f'#{tc} {result}')