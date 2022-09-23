# 가장 적은 비용으로 수영장을 이용할 수 있는 방법을 찾고
# 그 비용을 정답으로 출력하는 프로그램을 작성하라.
import sys
sys.stdin = open('sample_input (9).txt')
T = int(input())
for tc in range(1,T+1):
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
        # print(i, ': i의 값')
        # 3개씩 체크가 가능한 경우
        if i <= 9:
            if (arr[i]+arr[i+1]+arr[i+2])*li[0] > li[1]*3 or (arr[i]+arr[i+1]+arr[i+2])*li[0] > li[2]:
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
                visited[i] = 1
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
    # print(visited)
    if result > m3:
        result = m3

    print(f'#{tc} {result}')