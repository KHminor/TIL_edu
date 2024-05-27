# import sys
# input = sys.stdin.readline
# for _ in range(int(input())):
#     a,b = map(int,input().split())
#     _dic = {a:[1], b:[1]}
#     for i in [a,b]:
#         x, cnt = 1, 0
#         while x < i: # a 또는 b의 값이 x보다 작을 경우까지 찾기 
#             cnt+= 1
#             x += 2**cnt
#         # 2**cnt 는 시작 값, x는 끝 값 
#         s,e = 2**cnt, x
#         while e > s:
#             mid = (s+e)//2
#             if i >mid: # 찾을 노드 값이 mid 값보다 크다면
#                 s = mid+1
#                 _dic[i].append(_dic[i][-1]*2+1)
#             else: # 찾을 노드 값이 mid 값보다 작다면
#                 e = mid
#                 _dic[i].append(_dic[i][-1]*2)
#             if mid == i:
#                 _dic[i].append(mid)
#                 break
#     _set = set(_dic[a]).intersection(set(_dic[b]))
#     print(max(_set)*10) 

import sys
n = int(sys.stdin.readline())
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    while True:
        if a == b:
            print(a * 10)
            break
        if a > b:
            a //= 2
        else:
            b //= 2