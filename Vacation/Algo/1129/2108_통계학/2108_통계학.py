import sys

n = int(sys.stdin.readline())

li = []
for _ in range(n):
    li.append(int(sys.stdin.readline()))

li.sort()
st = list(set(li))
mxcnt = 0
num = []
for i in st:
    if li.count(i) > mxcnt:
        mxcnt = li.count(i)
        num = [i]
    elif li.count(i) == mxcnt:
        num.append(i)
num.sort()
print(num)
if len(li) > 1:
    print(round(sum(li)/n))
    print(li[(len(li)//n)+1])
    if len(num) > 1:
        print(num[1])
    else:
        print(num[0])
    print(max(li)-min(li))
else:
    print(li[0])
    print(li[0])
    print(li[0])
    print(0)