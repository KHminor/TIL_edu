import sys
sys.stdin = open('input.txt')
def push(x):
    stack.append(x)
    return

def pop():
    emp = size()
    if emp:
        pop = stack.pop()
        return pop
    else:
        return -1

def size():
    ln = len(stack)
    return ln

def empty():
    emp = len(stack)
    if emp:
        return 0
    else:
        return 1
def top():
    emp = len(stack)
    if emp:
        top = stack[-1]
        return top
    else:
        return -1

stack = []

T = int(input())
for _ in range(T):
    li = list(sys.stdin.readline().split())
    if li[0] == 'push':
        li[1] = int(li[1])
        push(li[1])

    elif li[0] == 'pop':
        print(pop())

    elif li[0] == 'size':
        print(size())

    elif li[0] == 'empty':
        print(empty())

    elif li[0] == 'top':
        print(top())