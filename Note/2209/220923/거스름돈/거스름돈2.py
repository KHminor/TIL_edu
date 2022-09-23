def coin(n,cnt):
    if n == 0:
        li.append(cnt)
    elif n < 0:
        return
    else:
        for i in range(5):
            coin(n-coin_types[i],cnt+1)


cnt = 0
m_cnt = 0
coin_types = [500, 400, 100, 50, 10]
n = 820
li = []
coin(n,cnt)
print(li)

# 안됨