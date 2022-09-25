# n = 4
# a = [i for i in range(1,n+1)]
#
# # 중복 X
# for i in range(n-2):
#     for j in range(i+1,n-1):
#         for x in range(j+1,n):
#             print(a[i],a[j],a[x])

# 중복
n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        for x in range(1,n+1):
            print(i,j,x)

# ====================================

# 가변 크기의 조합(재귀)
# def nCr(s,n,k):
#     if k == 0: print(p)
#     else:
#         for i in range(s,n-k+1):
#             p[k-1] = a[i]
#             nCr(i+1,n,k-1)
#
# n = 5
# a = [i for i in range(1,n+1)]
# print(a)
# p = [0]*3
# nCr(0,n,3)