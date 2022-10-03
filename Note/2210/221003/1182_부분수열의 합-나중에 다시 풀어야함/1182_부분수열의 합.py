n,s = map(int,input().split())
li = list(map(int,input().split()))
cnt = 0

llii = []
for i in range(1<<n):
    ch_li = []
    for j in range(n):
        if i & (1<<j):
            ch_li.append(li[j])
    # print(ch_li)
    if (sum(ch_li) == s or -1*sum(ch_li) == s) and ch_li not in llii:
        cnt += 1
        llii.append(ch_li)
        # print(llii)
    # print('=='*30)
print(len(llii))

# if s == 0:
#     print(cnt-1)
# else:
#     print(cnt)


# 대 실 패...