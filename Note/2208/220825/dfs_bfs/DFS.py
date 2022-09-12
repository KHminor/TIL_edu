from pprint import pprint
import sys
sys.stdin = open('input (2).txt')
# DFS
# 길 : 0, 벽 : 1, 출발점 : 2, 도착점 : 3
T = 10
N = 16
for _ in range(T):
    tc = int(input())                                       # 테스트 케이스 번호
    arr = [list(map(int,input())) for _ in range(N)]        # 배열 받기
    visited = [[0]*N for _ in range(N)]
    for i in range(N):                                      # 시작, 도착 좌표 찾기
        for j in range(N):
            if arr[i][j] == 2:
                si,sj = i,j
            elif arr[i][j] == 3:
                ei, ej = i, j

    result = 0
    stack = []
    while True:

        # 방문지점 체크
        visited[si][sj] = 1

        # 목표 지점 도착시 result = 1 저장 후 반복문 탈출
        if visited[ei][ej] == 1:
            result = 1
            break

        # 현재 좌표로 부터 상하좌우를 탐색 후 arr의 범위 안에서 벽이 아니며, 방문하지 않은 좌표의 경우 스택에 좌표 추가.
        for i,j in [[-1, 0], [1, 0], [0, -1], [0, 1]]:      # 상 하 좌 우 이동 경로 확인
            if 0 <= si+i < N and 0 <= sj+j < N and arr[si+i][sj+j] != 1 and not visited[si+i][sj+j]:
                stack.append([si+i,sj+j])

        # 스택이 비어있지 않다면 가장 뒤의 요소를 빼낸 후 si,sj에 할당
        if stack:
            si,sj = stack.pop()

        # 스택이 비어잇고 해당 조건문을 수행시 목표지점에 도달 하지 못한것이므로 result = 0 후 반복문 탈출
        else:
            result = 0
            break

    print(f'#{tc} {result}')