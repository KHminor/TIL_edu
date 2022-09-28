import sys
sys.stdin = open('sample_input (2).txt')

def bfs(n,m):
    visited[n] = 1
    q = [n]

    while q:
        n = q.pop(0)
        operator = [1,-1,n*2,n-10]

        for i in range(4):
            if operator[i] == m:
                return visited[n]
            if 0< operator[i] <= 1000000:
                if visited[operator[i]] == 0:
                    visited[operator[i]] = visited[n] +1
                    q.append(operator[i])
T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    li = []
    # bfs로 푸는 문제라고 한다.
    visited = [0]*1000001 # 이전에 해당 값이 나왔을 경우 계산x
    print(visited)