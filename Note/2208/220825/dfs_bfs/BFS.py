from pprint import pprint
import sys
sys.stdin = open('input (2).txt')
# BFS
# 길 : 0, 벽 : 1, 출발점 : 2, 도착점 : 3
T = 10
N = 16
for _ in range(T):
    tc = int(input())
    arr = [list(map(int,input())) for _ in range(N)]

    # 방문 체크 2차원 배열
    visited = [[0]*N for _ in range(N)]

    # 출발, 도착 좌표 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si,sj = i,j
            elif arr[i][j] == 3:
                ei,ej = i,j

    # 출력 결과 값 초기화
    result = 0
    # 큐 초기화
    q = []
    while True:
        
        # 현재 좌표 방문 체크
        visited[si][sj] = 1
        
        # 도착 지점의 좌표 방문시 반복문 탈출
        if visited[ei][ej] == 1:
            result = 1
            break
        
        # 해당 좌표로부터 상하좌우를 탐색후 arr를 벗어나지 않으며, 벽이 아니며, 방문하지 않은 곳의 좌표 q에 추가
        for i,j in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            if 0 <= si+i < N and 0 <= sj+j < N and arr[si+i][sj+j] != 1 and not visited[si+i][sj+j]:
                q.append([si+i,sj+j])
        
        # q가 비어있지 않다면 q의 가장 처음 값을 si,sj 에 각각 할당
        if q:
            si,sj = q.pop(0)
        # q가 비어있으며 해당 조건문을 수행시엔 목표지점을 방문하지 못했기에 result = 0 저장 후 반복문 탈출
        else:
            result = 0
            break

    print(f'#{tc} {result}')