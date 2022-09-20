import sys
sys.stdin = open('sample_input (3).txt')
T = int(input())
for tc in range(1,T+1):
    N = float(input())
    cnt = 1
    result = ''
    while cnt <= 12:
        N = N*2
        if N >= 1:
            N = N-1
            result += '1'
            if not N:
                break
        else:
            result += '0'
        cnt += 1
    if cnt == 13:
        result = 'overflow'
    print(f'#{tc} {result}')
