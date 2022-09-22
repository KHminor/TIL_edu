# 0시부터 다음날 0시 이전까지 A도크의 사용신청을 확인해
# 최대한 많은 화물차가 화물을 싣고 내릴 수 있도록 하면,
# 최대 몇 대의 화물차가 이용할 수 있는지
# 신청서에는 작업 시작 시간과 완료 시간이 매시 정각을 기준으로 표시되어 있고,
# 앞 작업의 종료와 동시에 다음 작업을 시작할 수 있다.

import sys
sys.stdin = open('sample_input (6).txt')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    li = []
    ch_li = [[0] for _ in range(25)]
    for _ in range(N):
        s,e = map(int,input().split())
        li.append(e)
        if ch_li[e] == [0]:
            ch_li[e] = [s]
        else:
            ch_li[e].append(s)
    li.sort()

    cnt = 1

    i = idx_i = idx_j = 0
    j = 1

    while j != N:
        for x in range(len(ch_li[li[j]])):
            ch_li[li[j]].sort()
            if li[i] <= ch_li[li[j]][x]:
                cnt += 1
                i = j
                break

        j += 1

    print(f'#{tc} {cnt}')

