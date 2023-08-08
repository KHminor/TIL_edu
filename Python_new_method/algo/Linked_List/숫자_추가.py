import sys
input = sys.stdin.readline
for i in range(int(input())): # TC cnt
    n,m,l = map(int,input().split())
    li = list(map(int,input().split()))
    for _ in range(m):
        idx,num = map(int,input().split())
        li = li[:idx]+[num]+li[idx:]
    print('#%d %d'%(i+1,li[l]))