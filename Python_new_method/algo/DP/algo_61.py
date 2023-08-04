a, b = input(), input()
if len(b) > len(a):
    tmp = a
    a = b
    b = tmp
dp = [0]*len(b)

for x in range(len(b)):
    state = 0
    for i in range(x, len(b)):
        if i == 0:
            for j in range(i, len(a)):
                if b[i] == a[j]:
                    dp[x] +=1
                    break
            if j == len(a)-1: break
        else:
            for j in range(i+1, len(a)):
                if b[i] == a[j]:
                    dp[x] +=1
                    break
            if j == len(a)-1: break
# 틀린 코드임