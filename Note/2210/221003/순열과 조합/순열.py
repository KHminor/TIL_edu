
# def nPr(s,n):
#     global result
#     run = triple = 0
#     if s == n:
#         if a[0] == a[1] == a[2]: triple += 1
#         if a[0]+2 == a[1]+1 == a[2]: run += 1
#         if a[3] == a[4] == a[5]: triple += 1
#         if a[3]+2 == a[4]+1 == a[5]: run += 1
#         if run+triple == 2:
#             result = True
#
#
#     else:
#         for i in range(s,n):
#             a[s],a[i] = a[i],a[s]
#             nPr(s+1,n)
#             a[s], a[i] = a[i], a[s]
#
# a = [2,3,5,7,7,7]
# n = 6
# result = False
# nPr(0,n)
# print(result)

# ===============================================

# def nPr2(s,n):
#     if s == n:
#         print(arr)
#     else:
#         for i in range(n):
#             if not visited[i]:
#                 visited[i] = 1
#                 arr[s] = li[i]
#                 nPr2(s+1,n)
#                 visited[i] = 0
#
#
# n = 5
# li = [i for i in range(1,n+1)]
# arr = [0]*n
# visited = [0]*n
# nPr2(0,n)

# ===============================================

def nPr3(s,n,k):
    if s == k:
        print(p)
    else:
        for i in range(n):
            if not visited[i]:
                visited[i] = 1
                p[s] = arr[i]
                nPr3(s+1,n,k)
                visited[i] = 0

n = 5
arr = [i for i in range(1,n+1)]
visited = [0]*n
k = 2
p = [0]*k
nPr3(0,n,k)