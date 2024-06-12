# 가짓수 구하는 문제
# li = [1,2,3,0,3] # 2
li = [1,2,0,3,0,3] # 4
# 1,3,5
# 1,4,5
# 2,3,5
# 2,4,5

n = sum(li)//3
result = 0
ln = len(li)
a,b,c = 0,0,0

for i in range(0,ln-2):
    a += li[i]
    if a != n: continue
    for j in range(i+1,ln-1):
        b += li[j]
        if b != n: continue
        for v in range(j+1,ln):
            c += li[v]
            if c != n: continue
            else:
                print(i,j,v)
                result += 1
                break
        c = 0
    b = 0
print(n)
print(result)