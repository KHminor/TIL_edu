n, ch_n = map(int,input().split())
li = [int(input()) for _ in range(n)]

ln =1
rn = max(li)

while ln<rn:
    num = (ln+rn)//2 +1
    cnt = sum([x//num for x in li])

    if cnt >= ch_n:
        ln = num
    else:
        rn = num-1

print(ln)