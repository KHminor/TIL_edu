import sys
sys.stdin = open('input.txt')
T = int(input())
for _ in range(T):
    ps_check = list(sys.stdin.readline())
    stack = []
    for i in range(len(ps_check)-1):        # sys.stdin.readline()을 사용하면 마지막에 개행 문자가 들어가기에 그 전까지만 반복
        if ps_check[i] == '(':              # i의 인덱스 값이 '('의 경우
            stack.append(ps_check[i])       # 현재 스택에 추가
        else:                               # i의 인덱스 값이 ')'의 경우
            if len(stack):                  # 만약 현재 stack에 요소가 있을 경우 스택의 마지막 요소를 빼내기
                stack.pop()                 
            elif len(stack) == 0:           # 만약 현재 stack에 요소가 없을 경우 
                stack = [1]                 # 현재 스택의 값을 요소가 하나 있도록 하며 반복문 종료
                break
    if not len(stack):                      # 현재 스택에 값이 없다면 YES 출력
        print('YES')
    else:                                   # 현재 스택에 값이 있다면 No 출력
        print('NO')