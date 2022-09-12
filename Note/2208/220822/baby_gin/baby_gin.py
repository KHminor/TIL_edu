# N = 667767, 054060, 101123

run = tri = 0
num = int(input())

li = [0]*10         # 0~9 까지의 숫자 카운팅하기 위한 list
while num > 0:
    li[num%10] += 1
    num = num//10
print(li)

for i in range(len(li)-2):
    while li[i] > 2:
        tri += 1
        li[i] -=3
    while li[i] >= 1 and li[i+1] >=1 and li[i+2] >= 1:
        run += 1
        li[i] -= 1
        li[i + 1] -= 1
        li[i + 2] -= 1
result = tri + run
if result == 2:
    print('baby-gin')
else:
    print('No')