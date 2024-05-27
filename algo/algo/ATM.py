# 뇌지컬
import sys
input = sys.stdin.readline
n = int(input())
result = 0
for i in sorted(map(int,input().rstrip('\n').split())):
    result += n*i
    n -= 1
print(result)

# dp 사용
li = sorted(map(int,input().rstrip('\n').split()))
for i in range(1,n): li[i] += li[i-1]
print(sum(li))