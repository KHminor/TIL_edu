
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
    if i <= 9:
        if (arr[i]+arr[i+1]+arr[i+2])*li[0] > li[1]*3 or (arr[i]+arr[i+1]+arr[i+2])*li[0] > li[2]:
            a_sum = (arr[i]+arr[i+1]+arr[i+2])*li[0]
            this_sum = a_sum

            j = 0
            x = 0
            while j < 10 :
                if visited[j] and visited[j+1] and visited[j+2]:
                    x = j
                    this_sum = (arr[j] + arr[j+1] + arr[j+2])*li[0]
                j += 1

            print(this_sum, ': this_sum')
            m3 += this_sum
            visited[x] = visited[x+1] = visited[x+2] = 0

            i += 2
        else:
            visited[i] = visited[i+1] = visited[i+2] = 0
            if li[1]*3 > li[2]:
                m3 += li[2]
                i += 2
            else:
                m3 += li[1]*3
                i += 2


    # 2개만 체크 가능한 경우
    elif i == 10:
        if (arr[i]+arr[i+1])*li[0] > li[1]*2 or (arr[i]+arr[i+1])*li[0] > li[2]:
            visited[i] = visited[i+1]= 0
            if li[1]*3 > li[2]:
                m3 += li[2]
                i += 1
            else:
                m3 += li[1]*3
                i += 1


    # 하나만 체크 가능한 경우
    else:
        if (arr[i])*li[0] > li[1] or (arr[i])*li[0] > li[2]:
            visited[i] = 0
            if li[1]*3 > li[2]:
                m3 += li[2]

            else:
                m3 += li[1]*3
        i += 1

    if i == 12: # 다 돌았을 때 아직
        for j in range(12):
            if visited[j] and arr[j]:
                if arr[j]*li[0] < li[1]:
                    m3 += arr[j]*li[0]

                else:
                    if li[1] < li[2]:
                        m3 += li[1]
                    else:
                        m3 += li[2]

    i += 1
    print(m3, ': m3')
    print(visited)
if result > m3:
    result = m3

print(f'#{result}')


# 10 100 50 300
# 0 0 0 0 0 0 0 0 6 2 7 8