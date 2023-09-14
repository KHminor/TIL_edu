import sys

input = sys.stdin.readline
n = int(input())
li = list(map(int,input().rstrip('\n').split()))
dp = [0]*n
dp[0] = li[0]

for i in range(1,n): dp[i] = max(dp[i-1]+li[i], li[i])
print(max(dp))

# import sys

# input = sys.stdin.readline
# n = int(input())
# li = list(map(int,input().rstrip('\n').split()))
# result = -sys.maxsize

# for i in range(n):
#     for j in range(i+1,n):
#         val = sum(li[i:j])
#         result = max(val,result)
# print(result)