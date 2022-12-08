import sys
n,m = map(int,sys.stdin.readline().split())
li = sorted(list(map(int,sys.stdin.readline().split())))
li.reverse()

cnt = li[0]-li[1]
li[0] = li[0]-cnt
while cnt != m:
    current = 0
    for i in range(len(li)-1):
        if li[i] != li[i+1]:
            current += 1
            break
        current += 1

    for j in range(current):
        li[j] -=1
        cnt += 1
        if cnt == m:
            break

print(li[0])