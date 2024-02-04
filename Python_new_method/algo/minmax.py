import sys
input = sys.stdin.readline

for i in range(int(input())):
    n = int(input())
    li = sorted(list(map(int,input().split())))
    print("#%d"%(i+1),li[-1]-li[0])