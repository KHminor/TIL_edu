import sys
n = int(sys.stdin.readline())
li = []
result = [0]*n
for i in range(n):
    x,y = map(int,sys.stdin.readline().split())
    li.append([x,y,i])

li.sort(key=lambda t:(t[0],t[1]) ,reverse=True)


for i in range(n):
    score = 1

    for j in range(n):
        if j == i: continue

        if li[i][0] < li[j][0] and li[i][1] < li[j][1]:
            score += 1

    result[li[i][2]] = score

print(*result)