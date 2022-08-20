import sys
sys.stdin = open('input.txt')
check = ['[',']' ,'(' ,')', '.']                    # 활호나 .이 아닌 경우에 반복문을 수행하지 않도록 하기 위한 list
str = list(sys.stdin.read().split('\n'))            # sys.stdin.read() 여러줄을 입력 받는 수행문이며, 개행 문자를 기준으로 분리
for j in str:                                       # str의 요소 하나씩 j에 저장
    stack = []                                      # 반복문 돌때마다 stack 초기화
    if j == '.':                                    # j의 값이 . 하나로 되어 있을 경우 반복문 종료.
        break
    for i in j:
        if not i in check:                          # 기존에 check하기 위한 것으로 i가 해당 요소중 하나가 아니면 다음으로 넘김
            continue
        if i == '[' or i == '(':                    # i가 [ or ( 의 경우 스택에 추가
            stack.append(i)
        elif i == ']':                              # i가 [ 의 경우
            if len(stack) and stack[-1] == '['  :   # 만약 스택에 뭔가 있으며 스택의 마지막 요소가 [ 의 경우 스택의 [ 를 빼내기
                stack.pop()
            else:                                   # 아닌 경우 스택에 요소 하나 집어 넣고 반복문 종료
                stack = [1]
                break
        elif i == ')':                              # 만약 스택에 뭔가 있으며 스택의 마지막 요소가 ( 의 경우 스택의 ( 를 빼내기
            if len(stack) and  stack[-1] == '(' :
                stack.pop()
            else:                                   # 아닌 경우 스택에 요소 하나 집어 넣고 반복문 종료
                stack = [1]
                break
        elif i == '.':
            break
    if stack:                                       # 스택에 뭔가 있을 경우 no
        print('no')
    else:                                           # 스택이 비워져 있을 경우 yes
        print('yes')
