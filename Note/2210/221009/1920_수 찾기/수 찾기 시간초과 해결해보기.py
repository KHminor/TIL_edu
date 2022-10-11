# 이분 탐색 해보자
# import sys
# sys.setrecursionlimit(2000)
#
# def two_find(x,s,e):
#     a = (s+e)//2
#     if li[a] == x or s == n-1 or e == 0:
#         if li[a] == x or x == li[s] or x == li[0]: return 1
#         else: return 0
#
#     elif x > li[a]:
#         return two_find(x,a,e)
#     elif x < li[a]:
#         return two_find(x,s,a)

import sys
n = int(sys.stdin.readline())
li = sorted(list(map(int,sys.stdin.readline().split())))

m = int(sys.stdin.readline())

for i in map(int,sys.stdin.readline().split()):
    s,e = 0,n
    while s<=e:
        a = (s + e) // 2
        if li[a] == i or s == n - 1 or e == 0:
            if li[a] == i or i == li[s] or i == li[0]:
                print(1)
                break
            else:
                print(0)
                break

        elif i > li[a]:
            s = a
        elif i < li[a]:
            e = a

