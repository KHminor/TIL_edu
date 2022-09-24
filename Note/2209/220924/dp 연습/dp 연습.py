a = [1,2,3,4,5]
ch_li = [0]*(len(a))


for i in range(len(a)):
    if i == 0:
        ch_li[i] = a[i]
    else:
        ch_li[i] = a[i] + ch_li[i-1]

print(ch_li)