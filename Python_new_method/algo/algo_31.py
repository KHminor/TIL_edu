# 개행을 추가해 푼 방식

a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)


# 반복문을 사용한 방식

a, b = map(int, input().strip().split(' '))
[print('*'*a) for i in range(b)]


