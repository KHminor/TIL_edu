# 일반적으로 푸는 방식
import sys
input = sys.stdin.readline
n = int(input())
a = sorted(map(int,input().rstrip('\n').split()))
b = sorted(map(int,input().rstrip('\n').split()),reverse=True)
print(sum([a[i]*b[i] for i in range(n)]))

# b를 정렬하지 않고 푸는 방식
import sys
input = sys.stdin.readline
n = int(input())
a = sorted(map(int,input().rstrip('\n').split()))
b = list(map(int,input().rstrip('\n').split()))
result, cnt = 0, 0
while b:
    b_mx = max(b)
    result += a[cnt]*b_mx
    del b[b.index(b_mx)]
    cnt += 1
print(result)