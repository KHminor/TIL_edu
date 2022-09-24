# # 아래 재귀로 만든 순열은 s부터 k개만큼의 순열을 만들기
# # 그래서 r_p의 s 숫자에 따라 앞의 숫자 a의 s인덱스 까지는 고정으로 두고
# # 순열을 생성
# def r_p1(s,k):
#     if s == k:
#         print(*a)
#
#     else:
#         for i in range(s,k):
#             a[s],a[i] =a[i],a[s]
#             r_p1(s+1,k)
#             a[s], a[i] = a[i], a[s]
#
#
#
# a = [1,2,3]
# r_p1(0,3)
# print('=='*10)

# =========================================================
#
# def r_p2(s,n):
#     if s == n:
#         print(p)
#
#     else:
#         for i in range(n): # 위 코드와의 차이는 계속해서 전체길이를 돈다는 점
#             if not visited[i]:
#                 visited[i] = 1
#                 p[s] = a[i]
#                 r_p2(s+1,n)
#                 visited[i] = 0
#
# n = 3   # 원하는 순열의 길이
# a = [i for i in range(1,n+1)]   # 리스트 생성
# p = [0]*n   # 원하는 순열의 값을 담을 리스트 초기화
# visited = [0]*n # 이전에 방문했는지 체크할 리스트 초기화
#
# r_p2(0,n)

# =========================================================

# 아래 코드는 n개 중에서 r개 만큼 고르는 재귀
def r_p3(s,n,r):
    if s == r:
        print(p)

    else:
        for i in range(n):
            if not visited[i]:
                visited[i] = 1
                p[s] = a[i]
                r_p3(s+1,n,r)
                visited[i] = 0


n = 5
r = 3

a = [i for i in range(1,n+1)]
p = [0]*r
visited = [0]*(n+1)
r_p3(0,n,r)

