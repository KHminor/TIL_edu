import sys
n,m = map(int,sys.stdin.readline().split())
li = sorted(list(map(int,sys.stdin.readline().split())))
li.reverse()

cnt = li[0]-li[1]
li[0] = li[0]-cnt

while cnt != m:

    current = 0
    for i in range(1,len(li)):
        if li[0] != li[i]:
            current += 1
            break
        current += 1

    if cnt+current >= m:
        li[0] -=1
        break
    else:
        for j in range(current):
            li[j] -=1
        cnt += current

print(li[0])