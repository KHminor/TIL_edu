import sys
sys.stdin = open('sample_input (2).txt')
T = int(input())
for tc in range(1,T+1):
    # N: 리스트 A, M: 리스트 B
    N,M = map(int,input().split())
    a_li = sorted(list(map(int,input().split())))
    b_li = list(map(int,input().split()))

    cnt = 0
    for i in b_li:
        l = ch_cnt = 0
        r = N-1
        m = (l + r) // 2
        if i == a_li[m]:
            cnt += 1
            continue

        while l < r:

            if i == a_li[m]: break
            elif i < a_li[m]:
                if not ch_cnt or ch_cnt == 2:
                    r = m-1
                    ch_cnt = 1
                else: break

            elif i > a_li[m]:
                if not ch_cnt or ch_cnt == 1:
                    l = m+1
                    ch_cnt = 2
                else: break
            m = (l + r) // 2
        if a_li[m] == i:
            cnt += 1

    print(f'#{tc} {cnt}')

# 이번 문제처럼 양쪽을 번갈아 체크해야 할 경우는
# 변수를 따로 두지 말고 하나를 두고 확인해보기!