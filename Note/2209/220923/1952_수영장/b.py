li = list(map(int,input().split()))
arr = list(map(int,input().split()))

m = 0
# 우선 한달을 기준으로 먼저 계산해보기
for i in range(12):
    if arr[i]:
        if arr[i]*li[0] < li[1] and arr[i]*li[0] < li[2]:
            m += arr[i]*li[0]

        else:
            if li[1] < li[2]:
                m += li[1]
            else:
                m += li[2]

if m > li[3]:
    m = li[3]
result = m

i = m3 = 0
visited = [1]*12
while i < 12:
    print(i, ': i의 값')
    # 3개씩 체크가 가능한 경우

    if i == 10:
        pass

    elif i == 11:
        pass

    else:
        for j in range(9):
            if visited[j] and visited[j+1] and visited[j+2]:
