import sys
sys.stdin = open('input (3).txt')
T = int(input())
for tc in range(1,T+1):
    s = input()
    li = []
    ssttrr = ''
    cnt = 0
    for i in s:
        if not i in li:
            li.append(i)
            ssttrr += i
    li = ''.join(li)
    print(len(li))
    print(li)
    for j in s:
        for i in li:
            if j == i:
                cnt += 1
    result = len(li)
    print(f'#{tc} {result}')

s = input()
