# import sys
# input = sys.stdin.readline

# n = int(input())
# m = int(input())
# li = list(map(int,input().rstrip('\n').split()))
# height = 0
# while True:
#     visit = [0]*(n+1)
#     cnt = 0
#     for i in li:
#         for j in range(i-height,i+height):
#             if 0<=j<n and not visit[j]: 
#                 visit[j] = 1
#                 cnt += 1
#     if cnt == n: 
#         print(height)
#         break
#     else: height+= 1

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
li = list(map(int,input().rstrip('\n').split()))
result = 0
if m == 1: result = max(li[0], n-li[0])
else:
    for i in range(m):
        if i == 0: result = max(li[i], result)
        elif i == m-1: result = max(n-li[i], result)
        else:
            _dif = li[i]-li[i-1]
            if not _dif%2: result = max(_dif//2, result)
            else: result = max(_dif//2+1, result)
print(result)