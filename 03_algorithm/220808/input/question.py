import sys

# question.py 실행시 파일 읽어옴
sys.stdin  = open('input.txt')

# 전체 TC 수 N
N = int(input())
# Ctrl + shift + f10
print(N)

# N 번만큼 입력받을  a 들을 각각 입력받아서
# 각 상황에 맞는 출력 결과를 만들어야한다.

for tc in range(1, N+1):
    a = int(input())

    if a % 2:
        result = '홀수'
    else:
        result = '짝수'
    print(f'#{tc} {result}')