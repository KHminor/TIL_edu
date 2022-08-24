import sys
sys.stdin = open('input (1).txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())             # N = Ai의 개수, M = Bj의 개수
    Ai = list(map(int,input().split()))
    Bj = list(map(int,input().split()))

                           
    if N > M:                                   # N 이 더 클 경우 
        chek_li = [0]*(N-M+1)                   # 값 저장할 리스트 초기화
        for i in range(N-M+1):
            for j in range(M):
                chek_li[i] += Ai[j+i]*Bj[j]     # 값 저장할 리스트의 해당 인덱스 값에 계속 더하기
    else:                                       # M 이 더 클 경우
        chek_li = [0] * (M-N+1)
        for i in range(M-N+1):
            for j in range(N):
                chek_li[i] += Ai[j] * Bj[j+i]
    max = 0                                     # 최대 값 구하기 위한 변수 초기화
    for j in chek_li:                           
        if j > max:                             # 현재 최대 값보다 클 경우 변경 
            max = j
    print(f'#{tc} {max}')