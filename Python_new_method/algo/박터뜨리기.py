# import sys
# def metho():
#     global last, hap
#     last += 1
#     hap += last


# input = sys.stdin.readline
# n,k = map(int,input().split())
# hap = 0
# last = 0
# if sum(range(1,k+1)) > n or k > n: print(-1)
# else:
#     if k%2: # 홀수
#         metho()
    
#     for i in range(k//2):
#         metho()
#         metho()
#         # 0 1 2 3 4
#         # 0 3 1 2 4
#     if hap == n: print(k-1)
#     else: print(hap, last)

import sys
input = sys.stdin.readline
n,k = map(int,input().split())
x = k*(k+1)//2
if x > n: print(-1)
elif (n-x)%k == 0: print(k-1)
else: print(k)