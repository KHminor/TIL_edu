import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque()
for _ in range(n):
    li = list(sys.stdin.readline().split())

    if li[0] == 'push':
        q.append(li[1])

    elif li[0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])

    elif li[0] == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])

    elif li[0] == 'pop':
        if not q:
            print(-1)
        else:
            print(q[0])
            q.popleft()

    elif li[0] == 'size':
        print(len(q))

    elif li[0] == 'empty':
        if len(q):
            print(0)
        else:
            print(1)


# 함수로 작성하는 것보다는 그냥 조건문으로 사용하는게 더 빠르고
# 큐를 만들어서 사용하는것보다 외장으로 만들어진거를 사용하는것이 더 빠르다..
# 어이없네