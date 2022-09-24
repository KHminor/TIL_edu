# 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는
# 방법의 수를 구하는 프로그램을 작성하시오.

# n :1 -> 1가지, n :2 ->2가지, n :3 -> 3가지, n: 4 -> 5가지,
n = int(input())

li = [0,1,2]

for i in range(n+1):
    if i <=2:
        continue
    else:
        li.append(li[i-2]+li[i-1])

if n <=2:
    print(li[n]%10007)
else:
    print(li[-1]%10007)


