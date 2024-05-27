# import sys
# from collections import deque
# input = sys.stdin.readline

# s = list(input().rstrip('\n'))+['']
# idx = len(s)-1
# ln = idx
# for _ in range(int(input())):
#     li = input().rstrip('\n').split()
#     if li[0] == 'L' and idx > 0: idx -= 1
#     elif li[0] == 'D' and idx < ln: idx += 1
#     elif li[0] == 'B' and idx > 0: 
#         s.pop(idx-1)
#         idx -= 1
#         ln -= 1
#     elif li[0] == 'P': 
#         s.insert(idx,li[1])
#         idx += 1
#         ln += 1
# print(''.join(s))

import sys
from collections import deque
input = sys.stdin.readline

l,r = deque(list(input().rstrip('\n'))),deque([])
for _ in range(int(input())):
    li = input().rstrip('\n').split()
    if li[0] == 'L' and len(l): r.appendleft(l.pop())
    elif li[0] == 'D' and len(r): l.append(r.popleft()) 
    elif li[0] == 'B' and len(l): l.pop()
    elif li[0] == 'P': l.append(li[1])
print(''.join(l+r))