num1, num2 = map(int,input().split())

big = 0
if num1 >= num2:
    big = num1
    num1_li = [0]*(num1+1)
    num2_li = [0]*(num1+1)
else:
    big = num2
    num1_li = [0]*(num2+1)
    num2_li = [0]*(num2+1)

cnt = 2
while num1 != 1:
    if not num1%cnt:
        num1_li[cnt] += 1
        num1 = num1//cnt
    else:
        cnt += 1
print(num1_li)
cnt_2 = 2
while num2 != 1:

    if not num2 % cnt_2:
        num2_li[cnt_2] += 1
        num2 = num2//cnt_2
    else:
        cnt_2 += 1
print(num2_li)

min = 1
max = 1


for i in range(2,big+1):
    if num1_li[i] != 0 or num2_li[i] != 0:
        # 최대 공약수
        if num1_li[i] <= num2_li[i]:
            min *= i**num1_li[i]
        else:
            min *= i**num2_li[i]

       # 최소 공배수
        if num1_li[i] >= num2_li[i]:
            max *= i**num1_li[i]
        else:
            max *= i**num2_li[i]
print(min)
print(max)