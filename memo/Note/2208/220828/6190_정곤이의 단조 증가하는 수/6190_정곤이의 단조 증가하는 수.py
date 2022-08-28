import sys
sys.stdin = open('s_input.txt')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    li = list(map(int,input().split()))

    i_arr = []

    for i in range(N-1):
        for j in range(i+1,N):
            i_arr.append(li[i] * li[j])
    max = -1
    for i in i_arr:
        num = i
        ch_li = []
        if i //10 <= 0:
            max = -1
            continue
        while i != 0:
            ch_li.append(i%10)
            i = i//10
        li = []
        for j in range(len(ch_li)):
            if not li:
                li.append(ch_li[j])
            else:
                if li[j-1] >= ch_li[j]:
                    li.append(ch_li[j])
                else:
                    break
        if li.count(li[0]) == len(li):
            continue
        if len(li) == len(ch_li) and num > max:
            max = num

    print(f'#{tc} {max}')
