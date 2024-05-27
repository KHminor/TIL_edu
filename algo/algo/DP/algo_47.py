def cycle(n):
    global cnt
    if n == 0: 
        cnt += 1
        return 
    for i in range(1,4): # 1~3까지의 수만으로 입력하기에
        if n-i >= 0: cycle(n-i)

for i in range(int(input())):
    n = int(input())
    cnt = 0
    cycle(n)
    print(cnt)


# for _ in range(int(input())):
#     n = int(input())
#     dp = [0]*11
#     dp[1], dp[2], dp[3] = 1, 2, 4
#     for i in range(4, n+1):
#         dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
#     print(dp[n])