# 딱 나누어 떨어지지 않을 경우엔 이라는 조건이 꼭 필요했었음;;
import sys
a,b,v = map(int,sys.stdin.readline().split())

if (v-a)%(a-b):
    print(((v-a)//(a-b))+2)
else:
    print(((v-a)//(a-b))+1)
