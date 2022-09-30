# ddz=z=
# nljj
n = list(input())
sch_li = ['c','d','l','n','s','z']
ch_li = ['-','=','j']

cnt = i = 0
while i != len(n):
    if n[i] in sch_li:
        if n[i] == 'd':
            if n[i:i+2] == 'd-':
                cnt += 1
                i += 2
                continue
            else:
                if n[i:i + 3] == 'dz=':
                    cnt += 1
                    i += 3
                    continue
        elif n[i] in ['c','s','z']:
            if n[i:i+1]

# 조건이 이렇게 원래 많으려나...

print(cnt)