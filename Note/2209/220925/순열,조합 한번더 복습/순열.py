# 고정 크기의 순열(크기에 따른 반복문 사용)
# a = [1,2,3]
# for i in a:
#     for j in a:
#         if i == j: continue
#         for x in a:
#             if i==x or j==x: continue
#             print(i,j,x)
# print()
# =================================================

# 가변 크기의 순열(재귀)
# def p1(s,n):        # s: 시작위치, n: 전체 크기
#     if s == n: print(*a)
#     else:
#         for i in range(s,n):
#             a[s], a[i] = a[i], a[s]
#             p1(s+1,n)
#             a[s], a[i] = a[i], a[s]
# n = 3
# a = [i for i in range(1,n+1)]
# p1(0,n)
# print()

# =================================================

# 가변 크기의 순열(재귀,방문 체크 방법) 이 방법대로 하면 반복문을 사용한 것과 같은 출력 결과가 나옴

# def p2(s,n):
#     if s == n: print(*p)
#     else:
#         for i in range(n):
#             if not visited[i]:
#                 visited[i] = 1
#                 p[s] = a[i]
#                 p2(s+1,n)
#                 visited[i] = 0
# n = 3
# a = [i for i in range(1,n+1)]
# visited = [0]*n
# p = [0]*n
# p2(0,n)
# print()

# =================================================

# 가변 크기의 순열(재귀, 원하는 위치 이후로만 순열 만들기)

def p3(s,n,k):
    if s == k: print(*p)
    else:
        for i in range(n):
            if not visited[i]:
                visited[i] = 1
                p[s] = a[i]
                p3(s+1,n,k)
                visited[i] = 0

n = 5
k = 3
a = [i for i in range(1,n+1)]
visited = [0]*n
p = [0]*k
p3(0,n,k)
print()
