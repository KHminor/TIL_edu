# import sys
# input = sys.stdin.readline
# n,k = map(int,input().split())
# li = sorted([int(input()) for _ in range(n)])
# recent = 0
# if n == 1: print(li[0]+k)
# else:
#     for i in range(1,n):
#         if k >= (li[i]-li[i-1])*i:
#             k = k-((li[i]-li[i-1])*i)
#             for j in range(0,i): 
#                 li[j] += li[i]-li[j]
#         elif k >= i:
#             li[0] +=  k//i
#             break
# print(li[0])

import sys
input = sys.stdin.readline
n,k = map(int,input().split())
li = [int(input()) for _ in range(n)]

start = min(li)
end = start+k

result = 0
while end >= start:
    mid = (start+end)//2

    hap = 0
    for i in li:
        if mid >i: hap += mid-i
    
    if k >= hap:
        start = mid+1
        result = max(mid,result)
    else: end = mid-1
print(result)