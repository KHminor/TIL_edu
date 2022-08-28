import sys
sys.stdin = open('sample_input.txt')
T = int(input())
# N : 과목 개수
# K : 선택 과목 개수
for tc in range(1,T+1):
    N,K = map(int,input().split())

    test_li = list(map(int,input().split()))

    sum = 0
    # 버블 정렬
    # for i in range(N-1,0,-1):
    #     for j in range(N-1):
    #         if test_li[j] > test_li[j+1]:
    #             test_li[j] ,test_li[j+1] = test_li[j+1], test_li[j]
    test_li.sort()
    for _ in range(K):
        sum += test_li.pop()
    print(f'#{tc} {sum}')