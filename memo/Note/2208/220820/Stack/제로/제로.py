import sys
sys.stdin = open('input.txt')
T = int(sys.stdin.readline())
stack = []                          # 스택 초기화
for _ in range(T):
    num = int(sys.stdin.readline()) # 입력값 추가
    if num:                         # 입력 받은 값이 0이 아닌 경우 스택에 추가
        stack.append(num)
    else:                           # 0일 경우 stack의 마지막 요소 반환
        stack.pop()
print(sum(stack))                   # 스택의 모든 값을 더하여 출력


