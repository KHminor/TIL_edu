import sys
sys.stdin = open('input.txt')
def push(x):                    # push 함수
    stack.append(x)             # 파라미터 값을 스택에 추가
    return

def pop():                      # pop 함수
    emp = size()                # size 함수의 리턴 값을 emp에 담기
    if emp:                     # emp의 값이 있다면
        pop = stack.pop()       # 마지막 값을 빼낸 후 pop에 값 추가
        return pop              # 해당 pop값을 리턴
    else:                       # emp의 값이 0의 경우
        return -1               # -1을 리턴

def size():                     # size 함수
    ln = len(stack)             # 스택의 현재 길이를 ln에 담기
    return ln                   # ln값을 리턴

def empty():                    # empty 함수
    emp = len(stack)            # size 함수의 리턴 값을 emp에 담기
    if emp:                     # emp의 값이 있다면
        return 0                # 0을 리턴
    else:                       # 없다면
        return 1                # 1을 리턴
def top():                      # top 함수
    emp = len(stack)            # size 함수의 리턴 값을 emp에 담기
    if emp:                     # emp의 값이 있다면 
        top = stack[-1]         # 스택의 마지막 요소를 top에 담기
        return top              # top을 리턴
    else:                       # 비어있다면
        return -1               # -1을 리턴

stack = []

T = int(input())
for _ in range(T):
    li = list(sys.stdin.readline().split())
    if li[0] == 'push':         # 입력 받은 값의 인덱스 0의 값이 push의 경우
        li[1] = int(li[1])      # 인덱스 1의 값을 정수화 하여
        push(li[1])             # 해당 값을 argument로 사용

    elif li[0] == 'pop':
        print(pop())

    elif li[0] == 'size':
        print(size())

    elif li[0] == 'empty':
        print(empty())

    elif li[0] == 'top':
        print(top())