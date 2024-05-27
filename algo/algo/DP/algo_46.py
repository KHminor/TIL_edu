# n = int(input())
# li = [ i if i == 1 else 0 for i in range(n+1)]
# for i in range(2, n+1):
#     li[i] = li[i-2] + li[i-1]
# print(li[-1])


# for _ in range(int(input())+1):
#     a,b = a+b, a
# print(b)

# a,b = 0,1
# m, p = 1000000, 1500000
# for _ in range((int(input())+1)%p):
#     a, b = (a+b)%m, a%m
# print(b)