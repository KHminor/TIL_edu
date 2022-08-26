T = int(input())
# N : 사람의 수
# M : 만드는 시간
# K : M의 시간당 만들 수 있는 개수
for tc in range(1, T+1):
    N,M,K = map(int,input().split())
    li = list(map(int,input().split()))
    # 버블 정렬(오름차순 만들기)
    for i in range(N-1,0,-1):
        for j in range(N-1):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1], li[j]
print(li)
# i = 0
# flag = 1
# while True:
#     if flag == 0:
#         break
#     i += 1
#     # 현재 시간
#     time = M*i
#     # 만든 개수
#     cnt = K*i
#
#     while True:
#         if li:
#             if li[0] >= time :
#                 cnt -= 1
#                 li.pop(0)
#                 if cnt <= 0:
#                     flag = 0
#                     result = 'Impossible'
#                     break
#             else:
#                 flag = 0
#                 result = 'Impossible'
#                 break
#         else:
#             flag = 0
#             result = 'Possible'
#             break
# print(result)