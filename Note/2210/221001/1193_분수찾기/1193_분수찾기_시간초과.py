n = int(input())
a = b = 1
cnt = 0
result = []
while cnt != n:
    s = a+b
    if (s-1)%2:     # 홀수의 경우
        for i in range(1,s):
            b,a = i,s-i
            cnt += 1
            if cnt == n: break
        result = [a,b]
        a,b = a+1,b
    else:     # 짝수의 경우
        for i in range(1,s):
            a,b = i,s-i
            cnt += 1
            if cnt == n: break
        result = [a,b]
        a,b = a,b+1

print(str(result[0])+'/'+str(result[1]))



