# def solution(number):
#     ln, cnt = len(number), 0
#     for i in range(ln-2):
#         for j in range(i+1, ln-1):
#             for z in range(j+1, ln):
#                 if number[i]+number[j]+number[z] == 0: cnt+= 1
#     return cnt

from itertools import combinations

def solution (number) :
    cnt = 0
    for i in combinations(number,3) :
        if sum(i) == 0 :
            cnt += 1
    return cnt

print(solution([0, 0, 1, -1, 0]))