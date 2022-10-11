# 시간 초과
import sys

n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))

m = int(sys.stdin.readline())

for i in map(int,sys.stdin.readline().split()):
    if li.count(i): print(1)
    else: print(0)


