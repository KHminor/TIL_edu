# 트리를 만들어서 풀어보자
import sys
from collections import deque
sys.stdin = open('sample_input (1).txt')
T = int(input())

from pprint import pprint
for tc in range(1,T+1):
    n,e = map(int,input().split())

    move = [[]*(n+1) for _ in range(n+1)]
    visited = [[1000000 ]*(n+1) for _ in range(n+1)]
    visited[0][0] = 0
    result = 0

    for _ in range(e):
        p,c,w = map(int,input().split())
        move[p].append([c,w])

    q = deque([[0,0]])     # 간선, 가중치
    while q:
        v,w = q.popleft()
        for mv,mw in move[v]:
            # 해당 좌표로 값 넣기
            dnt = w + mw
            if mv == n:
                if visited[v][mv] > dnt:
                    visited[v][mv] = dnt    # 현재
                    if not result:
                        result = dnt
                    else:
                        if result > dnt:
                            result = dnt
                continue
                    # print(result)
            else:
                visited[v][mv] = dnt
                q.append([mv,dnt])

    print(f'#{tc} {result}')

    # 0.26473s