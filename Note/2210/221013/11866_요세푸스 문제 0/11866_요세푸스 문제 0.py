import sys
n,k = map(int,sys.stdin.readline().split())
li = [i for i in range(1,n+1)]
print('<', end='')
cnt = k-1
i = 0
while i != n:
    if li[cnt] == 0:
        while True:
            cnt += 1
            if li[cnt] != 0:
                break

    print(li[cnt], end=', ')
    li[cnt] = 0
    if cnt+k > n:
        cnt = (cnt+k)%n
    else:
        cnt += k

    i += 1
print()