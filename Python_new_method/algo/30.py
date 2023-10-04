# import sys
# from itertools import permutations
# input = sys.stdin.readline
# n = sorted(list(input().rstrip('\n')),reverse=True)
# if '0' in n:
#     n.remove('0')
#     for i in (sorted(set(list(permutations(n,len(n)))),reverse=True)):
#         result = ''
#         for j in i:
#             result += j
#         if int(result)%30:
#             print(int(result)*10)
#             sys.exit(0)
#     print(-1)
# else: print(-1)

import sys
input = sys.stdin.readline
n = sorted(list(input().rstrip('\n')),reverse=True)
if '0' in n:
    result = ''
    for i in n: result += i 
    print(-1) if int(result)%30 else print(int(result)) 
else: print(-1)