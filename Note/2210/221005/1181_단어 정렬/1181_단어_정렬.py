import sys
n = int(sys.stdin.readline())
li = []
for _ in range(n):
    li.append(sys.stdin.readline()[:-1])
# li.sort()

ln = 1

ch_li = []
while ln != n:
    ct = []
    for i in li:
        if len(i) == ln and i not in ct:
            ct.append(i)
    ct.sort()
    for j in ct:
        ch_li.append(j)
    ln += 1

for i in ch_li:
    print(i)