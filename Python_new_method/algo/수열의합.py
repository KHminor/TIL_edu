# import sys
# from itertools import combinations
# n,l = map(int,input().split())

# state = False
# for i in range(l, 101):
#     for j in combinations(range(n+1),i):
#         li = sorted(list(j))
#         if sum(li) == n:
#             for x in range(1,len(li)):
#                 if li[x-1]+1 != li[x]: break
#                 elif x == len(li)-1 and li[x-1]+1 == li[x]:
#                     print(*li)
#                     sys.exit(0)

# if not state: print(-1)


import sys
N,L = map(int,input().split())

state = False
for l in range(L, 101):
    lx = N - (l*(l+1)//2)
    if not lx % l:
        x = lx//l
        if x + 1 >= 0: 
            print(*(i for i in range(x+1, x+l+1)))
            sys.exit(0)

if not state: print(-1)