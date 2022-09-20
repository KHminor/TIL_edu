# 암호코드는 8개의 숫자로 이루어져 있다.
# a = 88012346
import sys
sys.stdin = open('input (3).txt')

dic = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}
T = int(input())
for tc in range(1,T+1):
    # N: 세로, M: 가로
    N,M = map(int,input().split())
    ch = []
    for _ in range(N):
        bit = input().rstrip('0')
        if bit == '':
            continue
        elif ch:
            continue
        bit = list(bit)
        cnt = 1
        for _ in range(8):
            if cnt == 1:
                a = bit[-7*cnt:]
                a = ''.join(a)
                ch.append(a)
            else:
                a = bit[-7*cnt:-7*(cnt-1)]
                a = ''.join(a)
                ch.append(a)
            cnt += 1
        # break
    ch.reverse()
    # print(ch) # [[0, 1, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 1, 1], [0, 0, 0, 1, 1, 0, 1], [0, 1, 1, 0, 0, 0, 1], [0, 1, 1, 0, 0, 0, 1], [0, 1, 1, 1, 0, 1, 1], [0, 1, 1, 0, 0, 0, 1], [0, 1, 1, 1, 0, 1, 1]]
    li = []

    for i in ch:
        li.append(dic.get(i))

    s = gob = 0
    for j in range(len(li)):
        if j%2:
            s += li[j]
        else:
            gob += li[j]

    s = s + gob*3

    if s%10:
        result = 0
    else:
        result = sum(li)
    print(f'#{tc} {result}')