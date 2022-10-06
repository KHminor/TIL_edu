T = int(input())
for tc in range(1,T+1):
    n = int(input())
    li = list(map(int,input().split()))
    li.sort()
    resutl = 0
    if n == 1:
        result = li[0]*li[0]
    else:
        result = li[0]*li[n-1]
    print(f"#{tc} {result}")
