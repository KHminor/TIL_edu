import sys
sys.stdin = open('input1.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input()))

    cnt = 0
    c_li = [0]*N
    for i in range(N):
        if arr[i] == 1:
            cnt += 1
            c_li[i] = cnt
        else:
            cnt = 0

    max = 0
    for i in range(N):
        if c_li[i] > max:
            max = c_li[i]

    print(f'#{tc} {max}')
# 성공