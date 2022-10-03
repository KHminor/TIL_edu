n = int(input())
# cnt = 라인의 개수, ch_num = 지금까지의 분수의 개수, a/b
cnt = ch_num = a = b = 0
ch = 1 # 다음 라인의 요소 개수가 홀수

while True:
    cnt += 1
    if not ch_num+1 <= n <= ch_num+cnt:
        ch_num += cnt
        if ch == 1:
            ch = 2
        else:
            ch = 1
    elif ch_num+1 <= n <= ch_num+cnt:
        if ch == 1:
            for i in range(1,cnt+1):
                ch_num += 1
                a,b = cnt+1-i,i
                if ch_num == n: break
        else:
            for i in range(1,cnt+1):
                ch_num += 1
                b,a = cnt+1-i,i
                if ch_num == n: break
        break
print(str(a)+'/'+str(b))
