import sys
input = sys.stdin.readline
n = int(input())
li = list(map(int,input().split()))
dp = [1]*n
for i in range(1, n):
    for j in range(i):
        if li[i] > li[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(dp)

# [30, 10, 20, 10, 20, 60, 20, 10, 30, 50]