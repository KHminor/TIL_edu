# 2차원 캐시를 통해 푸는 방법
a,b = input(), input()
ln_a, ln_b = len(a), len(b)
dp = [[0]*(ln_b+1) for _ in range(ln_a+1)]
for i in range(1, ln_a+1):
    for j in range(1, ln_b+1):
        if a[i-1] == b[j-1]: dp[i][j] = dp[i-1][j-1]+1
        else: dp[i][j] = max(dp[i-1][j], dp[i][j-1]) 
print(max(dp[-1]))

# 1차원 캐시를 통해 누적하는 방법
a,b = input(), input()
ln_a, ln_b = len(a), len(b)
dp = [0]*ln_b
for i in range(ln_a):
    cnt = 0
    for j in range(ln_b):
        if dp[j] > cnt: 
            cnt = dp[j]
        elif a[i] == b[j]: 
            dp[j] = cnt + 1
print(max(dp))