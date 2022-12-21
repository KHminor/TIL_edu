n = int(input())
# 현재 채널에서 +,- 로 이동한 결과
result = abs(100-n)
m = int(input())
if m:
    broken = list(input().split())
else:
    broken = []

# 근데 여기서 이동하려는 채널이 0 <= i <= 500,000 인데
# 작은수에서 큰수로 이동때가 아닌 반대로 큰수에서 작은수로 내려오는 것까지 고려해야하는 걸까...?

for i in range(1000001):
    for j in str(i):
        if j in broken:
            break
    else:
        result = min(result, len(str(i))+abs(n-i))

print(result)
