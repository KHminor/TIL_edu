import sys
def two_find(x,s,e):
    if s >e:
        return 0
    a = (s+e)//2
    if x == li[a]: return 1
    elif x < li[a]:
        return two_find(x,s,e-1)
    else:
        return two_find(x,a+1,e)


n = int(sys.stdin.readline())
li = sorted(list(map(int,sys.stdin.readline().split())))

m = int(sys.stdin.readline())

for i in map(int,sys.stdin.readline().split()):
    print(two_find(i,0,n-1))
