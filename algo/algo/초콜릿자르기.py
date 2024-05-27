# 1,1 = 0
# 2,2 = 3 => 1 + 2 
# 3,3 = 8 => 2 + 6
# 2,4 = 7 => 1 + 6

n,m = map(int,input().split())
print(n-1+n*(m-1))


print(n*m-1)