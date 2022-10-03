# def nCr(s,n,k):
#     if k == 0:
#         print(p)
#
#     else:
#         for i in range(s,n+1-k):
#             p[k-1] = li[i]
#             nCr(i+1,n,k-1)
#
# n = 5
# li = [i for i in range(1,n+1)]
# k = 2
# p = [0]*k
# nCr(0,n,k)




def nCr(s,n,k):
    if k == 0:
        print(sorted(ch_li))

    else:
        for i in range(s,n+1-k):
            ch_li[k-1] = li[i]
            nCr(i+1,n,k-1)

n = 5
k = 3
li = [i for i in range(1,n+1)]
print(li)
ch_li = [0]*k
nCr(0,n,k)

















