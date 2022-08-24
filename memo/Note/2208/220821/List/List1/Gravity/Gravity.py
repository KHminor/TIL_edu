import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    weith = int(input())
    li = list(map(int,input().split()))
    # print(li)
    result = 0
    for i in range(weith):
        max_h = weith - (i+1)
        for j in range(i+1, weith):
            if li[j] >= li[i]:
                max_h -= 1
        if max_h > result:
            result = max_h
    print(f'#{tc} {result}')
