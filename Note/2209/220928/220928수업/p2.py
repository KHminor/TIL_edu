'''
1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7
'''

arr = list(map(int,input().split(',')))
li = [[] for _ in range(max(arr)+1)]
visited = [0]*(max(arr)+1)
for i in range(len(arr)//2):
    li[arr[i*2]].append(arr[i*2+1])
    li[arr[i*2+1]].append(arr[i*2])
result = []
v = 1
q = [v]
while q:
    v = q.pop(0)
    if visited[v] == 1: continue
    visited[v] = 1
    result.append(v)
    for i in li[v]:
        if visited[i] == 1: continue
        else:
            q.append(i)

print(result)