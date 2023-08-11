def bag(i, wei,val):
    global m_weight, m_value, k
    # 가치가 더 높고, 무게를 초과하지 않았을 경우 가치를 변경
    if val > m_value and k >= wei: m_value = val
    # 무게를 초과했을 경우 리턴
    elif wei > k: return
    
    for j in range(i, n):
        bag(j+1,li[j][0]+wei,li[j][1]+val)
        

import sys
input = sys.stdin.readline
n,k = map(int,input().split()) # 개수, 최대 무게
li = [ list(map(int,input().split())) for _ in range(n)] # 무게, 가치
m_value = 0
# 재귀 방식으로 풀어본다면
# 조건문으로 무게가 넘치지 않았고 현재 가치보다 누적해온 가치가 더 크다면 변경

bag(0,0,0)
print(m_value)


import sys
input = sys.stdin.readline
n,k = map(int,input().split())
li = [[0,0]]+[list(map(int,input().split())) for _ in range(n)]
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        weight, value = li[i]
        if j < weight: dp[i][j] = dp[i-1][j]
        else: dp[i][j] = max(value+dp[i-1][j-weight], dp[i-1][j])
print(max(dp[n]))