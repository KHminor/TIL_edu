cnt = 0
m_cnt = 0
coin_types = [500, 400, 100, 50, 10]
li = []

for i in range(5):
    n = 820
    cnt = 0
    while n > 0:
        for j in range(i,5):
            if n >= coin_types[j]:
                n -= coin_types[j]
                cnt += 1
                break
    print(cnt)