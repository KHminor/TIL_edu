n = int(input())
cnt = 0
s = '666'
i = 0
while True:
    if s in str(i):
        cnt += 1
        if cnt == n:
            break
    i+=1
print(i)


# 그냥 666이 들어가는 숫자를 처음부터 카운팅하면 되는거였음...