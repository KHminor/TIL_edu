# def nCm(s,n,m):
#     if m == 0:
#         print()
from itertools import combinations
n,m = map(int,input().split())
li = [i for i in range(1,n+1)]
print(len(list(combinations(li,m))))