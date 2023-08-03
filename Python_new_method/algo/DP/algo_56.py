import sys
from itertools import combinations
input = sys.stdin.readline
for i in range(int(input())):
    n,m = map(int,input().split())
    print(len(list(combinations([i for i in range(m)],n))))

# 조합의 공식으로 nCm의 경우엔
# n!/(n-m)!*m!

# import sys
# from math import factorial
# input = sys.stdin.readline
# for _ in range(int(input())):
#     n,m = map(int,input().split())
#     print(int(factorial(m)/(factorial(m-n)*factorial(n))))
#     print(int(factorial(m)/(factorial(m-n)*factorial(n))))