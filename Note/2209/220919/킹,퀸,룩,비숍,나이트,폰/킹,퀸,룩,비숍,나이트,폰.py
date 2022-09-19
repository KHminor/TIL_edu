# 킹 : 1 , 퀸 : 1, 룩 : 2, 비숍 : 2, 나이트 : 2, 폰 : 8

donghuk = list(map(int,input().split()))
a = [1, 1, 2, 2, 2, 8]
ch_li = []
for i in range(len(a)):
    result = a[i]-donghuk[i]
    ch_li.append(result)
print(*ch_li)