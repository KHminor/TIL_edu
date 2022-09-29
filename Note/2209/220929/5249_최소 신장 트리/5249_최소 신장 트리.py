from pprint import pprint
# T = int(input())
# n+1: 노드 수, e: 간선의 수
n,e = map(int,input().split())
# arr: 연결 노드의 가중치 [가중치 최대*간선의 수], ch_li: 연결된 노드 체크
arr = [[10000000]*(n+1) for _ in range(n+1)]
ch_li = [[0]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)
li = [0]*(n+1)
for x in range(e):
    i,j,w = map(int,input().split())
    # 양 방향으로 값을 넣어주기
    arr[i][j] = arr[j][i] = w
    ch_li[i][j] = ch_li[j][i] = 1
s = e = 0
while True:     # True 조건 변경하기
    visited[s][e] = 1
    for x in range(n+1):
        if ch_li[s][x] and not visited[s][x]:
            li.append(arr[s][x])


pprint(arr)
pprint(ch_li)
