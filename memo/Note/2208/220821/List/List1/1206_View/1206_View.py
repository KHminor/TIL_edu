import sys
sys.stdin = open('input.txt')
T = 10
for tc in range(1, T+1):
    N = int(input())
    li = list(map(int,input().split()))
    cnt = 0
    for i in range(2, N-2):
        if li[i] > li[i-2] and li[i] > li[i-1] and li[i] > li[i+1] and li[i] > li[i+2]:
            max_tw = [li[i-2], li[i-1], li[i+1], li[i+2]]
            cnt += li[i] - max(max_tw)
    print(f'#{tc} {cnt}')
