# 이번 문제의 교훈: 문제를 보고 최대 몇개의 라는 말과 같은 ~~ 나왔을때
# counting 하는 방법으로 해당 값을 li의 idx와 같게 하여 1 증가하는 형식으로
# 카운팅 하는 방법이 제일 좋을 것 같다.
# 그리고 문제를 꼼꼼히 읽어서 이해가 안가면 우선 이해부터 하고 손코딩을 해야
# 후에 들이는 시간이 줄어들것 같다.

import sys
sys.stdin = open('sample_in.txt')
T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ch_li = [[] for _ in range(N)]
    li = [0]*1001
    # print(li)
    for i in range(N):
        # s :출발, e :도착
        s, e = arr[i][1], arr[i][2]
        li[s] += 1
        li[e] += 1

        # 일반 버스
        if arr[i][0] == 1:
            for j in range(s+1,e):
                li[j] += 1

        # 급행 버스
        elif arr[i][0] == 2:
            for j in range(s+1,e):
                # s 가 짝수의 경우, j 또한 짝수만 추가
                if not s % 2 and not j % 2 :
                    li[j] += 1
                # s 가 홀수의 경우, j 또한 홀수만 추가
                elif s % 2 and  j % 2 :
                    li[j] += 1

        # 광역 급행 버스
        elif arr[i][0] == 3:
            for j in range(s+1, e):
                # s 가 짝수의 경우, j 는 4의 배수만 추가
                if not s % 2 and not j % 4:
                    li[j] += 1
                # s 가 홀수의 경우, j 는 3의 배수이면서 10의 배수가 아닌 것만 추가
                elif s % 2 and not j % 3 and j % 10:
                    li[j] += 1

    print(f'#{tc} {max(li)}')






