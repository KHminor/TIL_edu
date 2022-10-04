# T = int(input())
v,e = map(int,input().split())

dist = [10000000]*(v+1)
visited = [[] for _ in range(e)]
arr = [list(map(int,input().split())) for _ in range(e)]
arr.sort(key=lambda x:x[2])
print(arr)
print(visited)
print(dist)
print('=='*30)
cnt = x = 0
while cnt != v:
    n1,n2,w = arr[x]
    if not dist[n2] or dist[n2] > w:
        dist[n2] = w
        cnt += 1
    x += 1
print(dist)