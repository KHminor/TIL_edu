# n = int(input())
# for i in range(0, n-2):
#     for j in range(i+1, n-1):
#         for k in range(j+1, n):
#             print(1)
#         print('=====')
#     print('=====')

# 5, 4, 3, 2, 1
# 4, 3, 2, 1
# 3, 2, 1
# 2, 1
# 1

# s = 0
# for i in range(1, int(input())-1):
#     s += (i+1)*i//2
# print(s)

a,b = map(int,input().split())
c = int(input())
d = int(input())
print( 1 if a*d+b <= c*d and a<=c else 0 )