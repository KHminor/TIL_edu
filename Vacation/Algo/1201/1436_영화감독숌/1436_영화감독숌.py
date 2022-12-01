import sys

n = int(sys.stdin.readline())
cnt = chk = re_i = 0
state = 'false'
six = 0
while cnt != n:
    if chk % 10 != 6:
        cnt += 1
        chk += 1
    else:
        # 7부터 이상함
        for i in range(10):
            if cnt == n:
                state = 'true'
                re_i = i
                break
            elif i != 9:
                cnt += 1
            elif i == 9:
                cnt += 1
                chk += 2

    if state == 'true':
        break


if state == 'true':
    print(str(chk)+'66'+str(re_i))
else:
    print(str(chk-1)+'666')
