N = int(input()) + 1
N = list(range(N))
li = []
for i in N:
    li.append(str(i))
li = li[1:]

li_num = ['3','6','9']

result = []

for i in li:
    s = ''
    for j in i:
        if j in li_num:
            s += '-'
        else:
            s += j
    if 1 == s.count('-'):
        s = '-'

    result.append(s)

result = ' '.join(result)
print(result)

