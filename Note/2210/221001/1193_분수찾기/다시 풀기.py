n = int(input())
cnt = ch_num = a = b = 0
ch = 2
while ch_num != n+1:
    if n == 1:
        a,b = 1,1
        break
    if ch_num == n:
        if ch == 1:
            a,b = 1,cnt
        else:
            b,a = 1,cnt
        break
    elif ch_num-cnt == n:
        if ch == 1:
            a,b = cnt,1
        else:
            b,a = cnt,1
        break
    if not ch_num-cnt < n < ch_num:
        cnt += 1
        ch_num += cnt
        if ch == 1:
            ch = 2
        else:
            ch = 1
    elif ch_num-cnt < n < ch_num:
        ch_num -= cnt
        if ch == 1:
            for i in range(1,cnt+1):
                a,b = cnt+1-i,i
                ch_num += 1
                if ch_num == n: break
        else:
            for i in range(1,cnt+1):
                b,a = cnt+1-i,i
                ch_num += 1
                if ch_num == n: break

    print('cnt의 값:',cnt)
    print('ch_num의 값:',ch_num)
print(str(a)+'/'+str(b))



# 다시 생각해보기