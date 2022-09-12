import sys
sys.stdin = open('input (2).txt')
N = 100                                             # 가로 길이
T = 10
for tc in range(1, T+1):
    dump_cnt = int(input())                         # dump 가능한 횟수
    li = list(map(int,input().split()))             # 상자 높이
    for i in range(N-1,0,-1):                       # 버블 정렬을 통해 작은 크기부터 큰 순서로 나열
        for j in range(N-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1] , li[j]

    min = li[0]                                     # 현재 가장 작은 높이를 min
    max = li[-1]                                    # 현재 가장 높은 높이를 max
    ch_cnt = 0                                      # 덤프하여 적재한 cnt
    while dump_cnt:                                 # dump 가능한 횟수가 있을 경우까지

        for j in range(N):
            if dump_cnt == 0:                       # 만약 덤프 가능한 횟수가 0이면 반복문 탈출하기
                break                               
            if min == li[j]:                        # 현재 li의 j 인덱스 값이 min 값과 같을 경우  
                li[j] += 1                          # 현재 인덱스의 값을 1 증가
                ch_cnt += 1                         # 증가 한 만큼 카운트 개수를 1씩 증가
                dump_cnt -= 1                       # 덤프를 한 만큼 덤프 카운트를 1씩 감소
            else:                                   # 해당 li의 j 인덱스 값이 min과 같지 않을 경우 반복문 종료
                break
        min = li[j]                                 # min과 같이 않은 j 인덱스 값을 min 값으로 변경 

        while ch_cnt:                               # ch_cnt의 값이 존재할 동안 반복하기
            for j in range(N):
                if min == max:                      # min과 max 와 같을 경우 ch_cnt 를 0으로 만들고 바로 반복문 탈출
                    ch_cnt = 0
                    break
                if max == li[j]:                    # li의 j 인덱스 값이 max 와 같을 경우
                    li[j] -= 1                      # 해당 j 인덱스 값을 1 감소
                    ch_cnt -=1                      # 감소한 만큼 1 감소
                if ch_cnt == 0:                     # ch_cnt 의 값이 0일 경우 반복문 탈출
                    break
            max = li[-1]                            # max 값을 현재 li의 가장 마지막 값으로 변경
    result = max-min
    print(f'#{tc} {result}')
