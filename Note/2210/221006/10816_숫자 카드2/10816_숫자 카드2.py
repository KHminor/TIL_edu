import sys
n = int(sys.stdin.readline())
my_li = list(map(int,sys.stdin.readline().split()))
a = int(sys.stdin.readline())
ch_li = list(map(int,sys.stdin.readline().split()))

b = [0]*a
s_num = list((set(my_li) & set(ch_li)))

# for i in range(len(ch_li)):
#     if ch_li[i] in s_num:
#         print(my_li.count(ch_li[i]), end=' ')
#     else:
#         print(0, end=' ')

for i in range(len(ch_li)):
    if ch_li[i] in s_num:
        b[i] = my_li.count(ch_li[i])
    else:
        continue
print(*b)