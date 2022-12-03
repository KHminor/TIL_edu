# 현태한테 도움 요청하기

import sys
i = 500
# for i in range(1,222):
n = i
cnt = chk = re_i = 0
state = 'false'
six = 0
while cnt != n:
    print('여기?')
    if chk % 10 != 6:
        cnt += 1
        chk += 1
    else:
        if chk not in [66,666,6666]:
            for i in range(10):
                cnt += 1
                if cnt == n:

                    state = 'true'
                    re_i = i
                    break
                if i == 9:
                    chk += 1
        else:
            ln = len(str(chk))
            end = int('666'+(ln*'9'))+1
            start = int('666'+(ln*'0'))-1
            while start != end:
                print(cnt,start, end, chk)
                if cnt == n:
                    state = start
                    break
                start += 1
                cnt += 1
            chk += 2
    # print('여기는 cnt와 chk,state', cnt, chk,state)
    if state != 'false':
        break
    print('여기?')

if state == 'true':
    print(n,(str(chk)+'66'+str(re_i)))
elif state == 'false':
    print(n,(str(chk-1)+'666'))
    print('여기?')
else:
    print(cnt,state)
    # print('여기?')

