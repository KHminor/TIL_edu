# import sys
# sys.stdin = open('input (1).txt')
T = int(input())
# N : 사람의 수
# M : 만드는 시간
# K : M의 시간당 만들 수 있는 개수
for tc in range(1, T+1):
    N,M,K = map(int,input().split())
    li = list(map(int,input().split()))
    # 버블 정렬(오름차순 만들기)
    for i in range(N-1,0,-1):
        for j in range(N-1):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1], li[j]
    print(li)
    result = ''
    # M = M # 2초인 현재 상황에서
    bread = K   # 빵은 현재 2개
    for i in range(N):
        # print(i)
        if M == li[i]:
            bread -= 1  # 1개
            if i == N-1 and not bread:
                bread = 1
                # result = 'Possible'
                break
            elif i != N-1 and not bread:
                break
        elif M > li[i]:
            bread = 0
            break
        else:
            if i == 0:
                moc = li[i] // M
                # 현재 시간
                M = M * moc  # 264
                # 빵의 개수
                bread = bread - 1
            else:
                # 몫 구하기
                moc = li[i] // M
                # 현재 시간
                M = (li[i]-M )* moc  # 264
                # 빵의 개수
                bread = bread + moc * K -1
    if bread:
        result = 'Possible'
    else:
        result = 'Impossible'

    print(f'#{tc} {result}')

# 30 ,403, 547,