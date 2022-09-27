# import sys
# sys.stdin = open('input.txt')
# T = int(input())
# for tc in range(1,T+1):
n = int(input())
ch_li = [[] for _ in range(n+1)]
visited = [0]*(n+1)
move = [0]*(n+1)
for _ in range(n-1):
    p,c = map(int,input().split())
    ch_li[p].append(c)
    ch_li[c].append(p)

print(ch_li)
print(move)
# bfs 사용하기
q = [1]
while q:
    v = q.pop(0)
    if visited[v] == 1: continue

    visited[v] = 1

    for i in ch_li[v]:
        if visited[i] == 1: continue
        else:
            move[i] = v
            q.append(i)
    print(move)
# print(ch_li)
# print(visited)
# print(move)
# print('====================',tc,'====================')
for i in range(2,n+1):
    print(move[i])