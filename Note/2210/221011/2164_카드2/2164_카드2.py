import sys
from _collections import deque
n = int(sys.stdin.readline())
q = deque(list(i for i in range(1,n+1)))
while len(q) != 1:
    q.popleft()
    q.rotate(-1)
print(*q)


