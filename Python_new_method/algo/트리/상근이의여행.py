# import sys
# from collections import deque
# input = sys.stdin.readline
# for _ in range(int(input())): # tc
#     n,m = map(int,input().split()) # 국가수, 비행기 종류
#     _dic = {i:[] for i in range(1,n+1)}
#     visit = [0]*n
#     result = 0
#     for _ in range(m):
#         a,b = map(int,input().split())
#         _dic[a].append(b)
#         _dic[b].append(a)
    
#     for i in range(1,n+1):
#         if not visit[i]:
#             visit[i] = 1
#             q = deque(_dic[i])
#             while q:
#                 s = q.popleft()
#                 for j in _dic[s]:
                    
# 못품;; 담에 꼭 다시 풀자