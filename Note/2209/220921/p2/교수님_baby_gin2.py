'''
5
124783
667767
054060
101123
123123
'''

T = int(input())
for tc in range(1,T+1):
    card = int(input())
    c = [0]*12          # tri 검사를 쉽게 하기 위해서

    i = 0
    while i <6:
        c[card%10] += 1
        card //= 10
        i += 1

    tri = run = 0
    i = 0
    while i <10:
        if c[i] >= 3:
            c[i] -= 3
            tri += 1
            continue

        if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
            c[i] -=1
            c[i+1] -=1
            c[i+2] -=1
            run += 1
            continue
        i+= 1

    if run + tri == 2:
        print('Baby-gin!')
    else:
        print('False')