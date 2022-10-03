a,b,v = map(int,input().split())
d = distance = 0
while distance != v:
    if distance+a >= v:
        d += 1
        break
    else:
        distance = distance+a-b
        d += 1
print(d)