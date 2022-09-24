# 반복문을 사용한 조합
n = 10
for i in range(1,n-2):
    for j in range(i+1,n-1):
        for x in range(j+1,n):
            print(i,j,x)

# 위의 코드의 경우 고정 크기를 가진 조합으로
# i부터 x까지 나열한 것으로 순서에 상관이 없는 조합
# 나열할 조합의 크기에 따라 for문의 개수가 달라진다



