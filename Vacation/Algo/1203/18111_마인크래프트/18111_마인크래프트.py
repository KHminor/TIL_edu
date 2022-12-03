import sys
n,m,b = map(int,sys.stdin.readline().split())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
floor = []
ch_li = [0]*257
for i in range(n):
    for j in range(m):
        ch_li[arr[i][j]] += 1
        if arr[i][j] not in floor:
            floor.append(arr[i][j])
print(ch_li)
print(floor)