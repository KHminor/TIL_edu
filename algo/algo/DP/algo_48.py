import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

for i in range(1, n):
    arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + arr[i][0] # 빨강
    arr[i][1] = min(arr[i-1][0], arr[i-1][2]) + arr[i][1] # 초록
    arr[i][2] = min(arr[i-1][0], arr[i-1][1]) + arr[i][2] # 파랑
print(min(arr[n-1]))