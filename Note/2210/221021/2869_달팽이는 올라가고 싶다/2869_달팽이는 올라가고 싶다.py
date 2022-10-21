import sys

a,b,v = map(int,sys.stdin.readline().split())

result = (v-b)//(a-b) +1
print(result)

