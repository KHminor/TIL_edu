import sys
sys.stdin = open('sample_input.txt')
T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    push_K = list(map(int,input().split()))

    check = []                              # 리스트 초기화
    for i in range(1,N+1):                  # 1명 부터 N명까지
        if i not in push_K:                 # 제출한 학생이 아닌 경우만
            check.append(i)                 # check에 추가
    check = check
    print(f'#{tc}', end=' ')
    print(*check)
