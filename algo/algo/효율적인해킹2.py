import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().rstrip('\n').split())
_dic = {i:[] for i in range(n+1)}
li = [0]*(n+1)

for _ in range(m):
    a,b = map(int,input().rstrip('\n').split())
    _dic[b].append(a)

for i in range(1,n+1):
    visit = [0]*(n+1)
    visit[i] = 1
    q = deque([i])

    while q:
        s = q.popleft()
        for j in _dic[s]:
            if not visit[j]: 
                visit[j] = 1
                li[i] += 1
                q.append(j)
[print(i, end=' ') for i in range(len(li)) if max(li) == li[i]]