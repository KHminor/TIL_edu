num1, num2 = map(int,input().split())

big = 0
# 어떤 값이 더 큰지 확인 하기 위한 조건과 큰 값을 기준으로
# 약수들이 총 몇개가 있는지 체크하기 위한 arr 만들기
if num1 >= num2:
    big = num1
    num1_li = [0]*(num1+1)
    num2_li = [0]*(num1+1)
else:
    big = num2
    num1_li = [0]*(num2+1)
    num2_li = [0]*(num2+1)

# 2로 나누기 위한 변수
cnt = 2
# 2부터 시작해서 num1이 1이 될때까지 cnt 를 증가시키며 약수를 찾기
while num1 != 1:
    if not num1%cnt:
        num1_li[cnt] += 1
        num1 = num1//cnt
    else:
        cnt += 1
print(num1_li)

# 2로 나누기 위한 변수
cnt_2 = 2
# 2부터 시작해서 num2이 1이 될때까지 cnt_2 를 증가시키며 약수를 찾기
while num2 != 1:
    if not num2 % cnt_2:
        num2_li[cnt_2] += 1
        num2 = num2//cnt_2
    else:
        cnt_2 += 1
print(num2_li)

# 가장 큰 값과 가장 작은 값을 우선 1로 초기화
min = 1
max = 1

# 배열의 2부터 가장 큰 값까지 반복하며 
# num1_li[i] ,num2_li[i] 모두 0이 나올때까지 반복하며 최대 공약수와 최소 공배수를 찾기
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