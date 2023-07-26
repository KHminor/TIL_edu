# import sys
# input = sys.stdin.readline
# n,s = map(int,input().split())
# a = list(map(int,input().split()))
# cnt = 0
# for i in range(1 << n):
#     li = []
#     for j in range(n):
#         if i & (1<<j): li.append(a[j])
#     if sum(li) == s and li != []: 
#         cnt += 1
# print(cnt)
# ==================================

# from sys import stdin
# input = stdin.readline
# N, S = map(int, input().split())
# num = list(map(int, input().split()))
# cnt = 0
# ans = []
# def solve(start):
#     global cnt
#     if sum(ans) == S and len(ans) > 0:
#         cnt += 1

#     for i in range(start, N):
#         ans.append(num[i])
#         solve(i+1)
#         ans.pop()
# solve(0)
# print(cnt)

# ==================================

import sys
input = sys.stdin.readline
n,s = map(int,input().split())
a = list(map(int,input().split()))
cnt = 0
li = []
def subsequence(start):
    global cnt
    if sum(li) == s and li != []: cnt += 1
    for i in range(start, n):
        li.append(a[i])
        subsequence(i+1)
        li.pop()
subsequence(0)
print(cnt)