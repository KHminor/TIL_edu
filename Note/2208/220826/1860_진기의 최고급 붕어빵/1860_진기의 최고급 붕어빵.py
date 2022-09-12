# N : 사람의 수
# M : 만드는 시간
# K : M의 시간당 만들 수 있는 개수
import sys
sys.stdin = open('input (1).txt')
T = int(input())
for tc in range(1,T+1):
    N,M,K = map(int,input().split())
    li = list(map(int,input().split()))
    # 버블 정렬(오름차순 만들기)
    for i in range(N-1,0,-1):
        for j in range(N-1):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1], li[j]
    flag = 1
    idx = 1
    print(li)
    while True:
        make_li = li[:idx]
        max = make_li[-1]
        moc = max//M
        time = M*moc
        make_bread = moc*K
        for i in make_li :
            make_bread -= 1
            if idx == N and not make_bread < 0 :
                result ='Possible'
                flag = 0
                break
        if flag == 0:
            break
        if make_bread < 0:
            result = 'Impossible'
            break
        idx += 1
    print(f'#{tc} {result}')


