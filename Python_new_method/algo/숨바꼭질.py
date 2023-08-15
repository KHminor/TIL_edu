# q에 넣어서 하나씩 조사를 하며 방문한거라면 추가하지 않고, 
# 방문하지 않았을 때만 추가하면서, 추가시 방문 표시를 해서 중복으로 추가되지 않도록 하기
# 그리고 하나씩 어떤 조사를 할 것이나면, n-1, n+1, n*2 와 그 숫자에 대한 카운팅을 함께 넘겨주기
from collections import deque
n,k = map(int,input().split())
visit = [0]*100001
visit[n] = 1
q = deque([[n,0]])

while q:
    s,cnt = q.popleft()
    if s == k:
        print(cnt)
        break
    for ds in [s+1, s-1, s*2]:
        if 0<=ds<=100000 and not visit[ds]:
            visit[ds] = 1
            q.append([ds,cnt+1])
