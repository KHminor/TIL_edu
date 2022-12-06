import sys

m,n = map(int,sys.stdin.readline().split())
for i in range(m,n+1):
    state = False
    jegob = int(i**0.5)+1
    if i == 1:
        pass
    for j in range(2,jegob):
        if not i%j:
            state = True
            break
    if state == False:
        print(i)

