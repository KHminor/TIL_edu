'''
1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7
'''

arr = list(map(int,input().split(',')))
li = [[] for _ in range(max(arr)+1)]
visited = [0]*(max(arr)+1)
for i in range(len(arr)//2):
    li[arr[i*2]].append(arr[i*2+1])
    li[arr[i*2+1]].append(arr[i*2])
print(li)
result = []
v = 1
stack = [v]
while stack:
    v = stack.pop()
    if visited[v] == 1: continue
    visited[v] = 1
    result.append(v)
    # li[v].sort(reverse=True)     # 오름차순 정렬하면 [1, 2, 4, 6, 5, 7, 3]
    for i in li[v]:                # 하지 않으면 [1, 3, 7, 6, 5, 2, 4]
        if visited[i] == 1: continue
        else:
            stack.append(i)

print(result)