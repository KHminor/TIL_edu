def bfs(v, N, t):  # v 시작정점, N 마지막 정점 번호, t 찾는 정점
    visited = [0]*(N+1)
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        v = q.pop(0)
        if v == t:          # visit(v)
            return 1        # 목표 발견


tc, E = 1, 16
adjList = [[] for _ in range(100)]
arr = [0, 1, 0, 2, 1, 4, 1, 3, 4, 8, 4, 3, 2, 9, 2, 5, 5, 6, 5, 7, 7, 99, 7, 9, 9, 8, 9, 10, 6, 10, 3, 7]
for i in range(E):
    a, b, = arr[i*2], arr[i*2+1]            # i 를 기준으로 2개씩 끊어서 adjList의 인덱스 위치랑 a 의 값과 매칭을 시켜 연결되어있는 간선인 b를 추가
    adjList[a].append(b)
# print(adjList)

bfs(0, 99, 99)  # 시작, 마지막 정점, 목표 정점번호