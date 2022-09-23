# def f(n,x):
#     if n == x:
#         b.append(a[:])
#         # print(a)
#
#     else:
#         for j in range(n,x):
#             a[n],a[j] = a[j], a[n]
#             f(n+1,x)
#             a[n],a[j] = a[j], a[n]
#
# a = [1,2,3,4]
# b = []
# f(0,4)
# print(b)


# 조합

def c(i,j):
    if j == 0:
        print(ch)
    elif j > i: return

    else:
        ch[j-1] = a[i-1]
        c(i-1,j-1)
        c(i-1,j)


import itertools

a = [3,4,5,6,7]
result = itertools.product(a, repeat=3)
print(*list(result))




