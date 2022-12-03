n, cntn = map(int,input().split())

li = sorted([int(input()) for _ in range(n)])
ch_li = li[:]
cnt = result = 0
while True:
    for i in range(n):
        cnt += li[i]//ch_li[0]
    if cnt == cntn:
        result = ch_li[0]
        break
    else:
        ch_li[0] -= 1
        cnt = 0
# print(li)
# print(ch_li, cnt)
print(result)