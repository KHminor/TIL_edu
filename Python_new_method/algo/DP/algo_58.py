n = int(input())
dp = [0]*(n+1)
dp[0:3] = [0, 1, 1]
if n < 3: print(dp[n])
else:
    for i in range(3, n+1): dp[i] = dp[i-1]+dp[i-2]
    print(dp[-1])

n = int(input())
a, b = 1, 1
for _ in range(2, n): a, b = b, a+b
print(b)