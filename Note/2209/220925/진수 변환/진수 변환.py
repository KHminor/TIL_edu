n = 149
s = ''

# 10진수를 2진수로 변경
while n != 0:
    namugy= n%2

    s = str(namugy) + s
    n = n//2
print(int(s))

# 2진수를 8진수로 변경

for i in range(len(s)//3):