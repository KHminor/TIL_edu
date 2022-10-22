import sys
n = int(sys.stdin.readline())
li = []
result = [0]*n
for i in range(n):
    x,y = map(int,sys.stdin.readline().split())
    li.append([x,y,i])

li.sort(key=lambda t:(t[0],t[1]) ,reverse=True)
print(li)

cnt = 0
score = 1
while len(li) != 0:

    s = 0
    n = 1
    ln = len(li)
    result[li[s][2]] = score

    for _ in range(ln-1):
        if li[s][0] > li[n][0] and li[s][1] > li[n][1]:
            n += 1
        else:
            if li[s][0] > li[n][0] and li[s][1] > li[n][1]:
                cnt += 1
            result[li[n][2]] = score
            li.pop(n)
            cnt += 1


    score += cnt+1

    li.pop(s)

print(*result)