# 반복문 ( 고정 크기 )
# for i in range(1,4):
#     for j in range(1,4):
#         if i != j:
#             for k in range(1,4):
#                 if k != i and k != j:
#                     print(i,j,k)
#
#
# 재귀호출
# p[]: 데이터가 저장된 배열
# i:선택된 원소의 위치, k: 원소의 개수,
# def f(i, k):
#     global cnt
#     if i == k:      # 인덱스 i == 원소의 개수
#         cnt +=1
#         print(p)
#     else:
#         for j in range(i,k):
#             p[i], p[j] = p[j], p[i]
#             f(i+1,k)
#             p[i], p[j] = p[j], p[i]
# 
# cnt = 0
# p = [1,2,3]
# f(0,3)
# print(cnt)
# [1, 2, 3]
# [1, 3, 2]
# [2, 1, 3]
# [2, 3, 1]
# [3, 2, 1]
# [3, 1, 2]

# ==================================================
# 위아래 서로 다른 접근 순서이기에 둘다 알고 있어야 할 듯

# def f(i,k):
#     if i == k:
#         print(p)
#     else:
#         for j in range(k):      # uesd 는 처음부터 끝까지 가는 것니까
#             if used[j] == 0 :   # a[j] 가 아직 사용되지 않았으면
#                 used[j] = 1     # a[j] 가 사용됨으로 표시
#                 p[i] = a[j]     # p[i] 는 a[j] 로 결정
#                 f(i+1, k)       # p[i+1] 값을 결정하러 이동
#                 used[j] = 0     # a[j]를 다른 자리에서 쓸 수 있도록 해제
#
# N = 3
# a = [i for i in range(1,N+1)]
# p = [0]*N
# used = [0]*N
# f(0,N)
#
# [1, 2, 3]
# [1, 3, 2]
# [2, 1, 3]
# [2, 3, 1]
# [3, 1, 2]
# [3, 2, 1]


# ===============================================================================
# 아래는 N에서 R개 만큼만 고르는 경우
def f(i,n,r):
    if i == r:
        print(p)
    else:
        for j in range(n):      # uesd 는 처음부터 끝까지 가는 것니까
            if used[j] == 0 :   # a[j] 가 아직 사용되지 않았으면
                used[j] = 1     # a[j] 가 사용됨으로 표시
                p[i] = a[j]     # p[i] 는 a[j] 로 결정
                f(i+1, n,r)       # p[i+1] 값을 결정하러 이동
                used[j] = 0     # a[j]를 다른 자리에서 쓸 수 있도록 해제

N = 4
R = 3
a = [i for i in range(1,N+1)]
used = [0]*N
p = [0]*R
f(0,N,R)

# [1, 2]
# [1, 3]
# [2, 1]
# [2, 3]
# [3, 1]
# [3, 2]