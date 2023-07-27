import sys
input = sys.stdin.readline
n = int(input())
# 우선 첫날을 무조건 이용한다고 가정
start = hap = 0
li = [ list(map(int,input().split())) for _ in range(n)]
result = [li[0]]
while start <= n-1:
    t,p = result[-1]
    for i in range(start+1,start+t):
        if t > li[i][0] and p < li[i][1]: t,p = li[i][0], li[i][1]
    result[-1] = [t,p]
    start += t
    hap += p
    if start >= n or start+li[start][0] > n: break
    else: result.append(li[start])
print(hap)

# import sys
# N = int(input())

# schedule = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

# dp = [0 for i in range(N+1)]

# for i in range(N):
#     for j in range(i+schedule[i][0], N+1):
#         if dp[j] < dp[i] + schedule[i][1]:
#             dp[j] = dp[i] + schedule[i][1]

# print(dp)

# import sys
# input = sys.stdin.readline
# n = int(input())
# li = [list(map(int,input().split())) for _ in range(n)]
# dp = [0]*(n+1)

# for i in range(n):
#     for j in range(i+li[i][0], n+1):
#         if dp[j] < dp[i] + li[i][1]: dp[j] = dp[i] + li[i][1]
# print(dp[-1])


# import sys
# input = sys.stdin.readline
# n = int(input())
# li = [list(map(int,input().split())) for _ in range(n)]
# dp = [0]*(n+1)

# for i in range(n-1,-1,-1):
#     if i+li[i][0] > n: dp[i] = dp[i+1] # 기간이 지나면 현재까지의 가장 큰 값을 앞으로 전달
#     else: dp[i] = max(dp[i+1], li[i][1]+dp[i+li[i][0]])
# print(dp[0])

# Bottom up 
# import sys 
# input = sys.stdin.readline
# n = int(input())
# li = [list(map(int,input().split())) for _ in range(n)]
# dp = [0]*(n+1)

# for i in range(n):
#     for j in range(i+li[i][0], n+1):
#         if dp[j] < dp[i]+li[i][1]: dp[j] = dp[i]+li[i][1]
# print(dp[-1])

# Top Down
import sys 
input = sys.stdin.readline
n = int(input())
li = [list(map(int,input().split())) for _ in range(n)]
dp = [0]*(n+1)

for i in range(n-1,-1,-1):
    if i+li[i][0] > n: dp[i] = dp[i+1]
    else: dp[i] = max(dp[i+1], li[i][1]+dp[i+li[i][0]])
print(dp[0])