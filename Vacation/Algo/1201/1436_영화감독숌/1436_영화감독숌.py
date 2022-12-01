# 현태한테 도움 요청하기

import sys

for i in range(1,501):
    n = i
    cnt = chk = re_i = 0
    state = 'false'
    six = 0
    while cnt != n:
        if chk % 10 != 6:
            cnt += 1
            chk += 1
        else:
            for i in range(10):
                cnt += 1

                if cnt == n:
                    state = 'true'
                    re_i = i
                    break
                if i == 9:
                    chk += 1
        if state == 'true':
            break


    if state == 'true':
        print(n,(str(chk)+'66'+str(re_i)))
    else:
        print(n,(str(chk-1)+'666'))
