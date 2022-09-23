# 0번 부터 출발?
def dfs(n,s):
    stack = [n,s]
    while stack:
        n,s = stack.pop()




# T = int(input())
N,E = map(int,input().split())
arr = [[]*N for _ in range(N)]

for _ in range(E):
    s,e,d = map(int,input().split())
    arr[s].append([e,d])
# print(arr[0][0][0])
print(arr)

start = sum = 0
dfs(start,s)