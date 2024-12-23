import sys
input = sys.stdin.readline

n = int(input())
li = [int(input()) for _ in range(n)] # 가로수 위치
result = [0]*(n-1) # 가로수 거리 차이

for i in range(1,n): result[i-1] = li[i]-li[i-1]

# 최대 공약수
a = result[0]
for i in range(1,len(result)):
    b = result[i]
    while b!=0: a,b = b,a%b

print(sum([i//a-1 for i in result]))



# 4
# 1
# 5 
# 13
# 21

# 2 6 12 18