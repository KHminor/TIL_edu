import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    ch_li = [0]*10
    num = int(input())
    while num > 0:
        ch_li[num%10] += 1
        num = num//10
        if num == 0:
            ch_li[num % 10] += 1
    tri = run = 0
    # print(ch_li)
    for i in range(len(ch_li)):
        while ch_li[i] > 2:
            if ch_li[i] >= 3:
                tri += 1
                ch_li[i] -= 3

    for i in range(len(ch_li)-2):
        while ch_li[i] >= 1 and ch_li[i+1] >= 1 and ch_li[i+2] >= 1:
                run += 1
                ch_li[i] -= 1
                ch_li[i+1] -= 1
                ch_li[i+2] -= 1
    result = tri + run
    if result == 2:
        print(f'#{tc} baby-gin')
    else:
        print(f'#{tc} Nope')
