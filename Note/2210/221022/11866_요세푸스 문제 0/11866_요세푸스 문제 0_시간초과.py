import sys
k,n = map(int,sys.stdin.readline().split())

li = [i for i in range(1,k+1)]

rs_li = []

s = -1
while len(rs_li) != k:

    for _ in range(n):
        s += 1
        if s >= k:
            s %= k
        if li[s] in rs_li:
            while li[s] in rs_li:
                s += 1
                if s>=k:
                    s %= k


    rs_li.append(li[s])
print('<',end='')
for i in rs_li:
    if i != rs_li[-1]:
        print(str(i)+',', end=' ')
    else:
        print(str(i),end='')

print('>')