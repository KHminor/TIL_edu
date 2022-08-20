j = list(input())
check = ['[',']' ,'(' ,')', '.']
stack = []

cnt = 0
for i in j:
    if not i in check:
        continue
    print(i)
    if i == '[' or i == '(':
        stack.append(i)
    elif i == ']':
        if len(stack) and stack[-1] == '[':
            stack.pop()
        else:
            b_stack = [1]
            break
    elif i == ')':
        if len(stack) and stack[-1] == '(':
            stack.pop()
        else:
            s_stack = [1]
            break
    elif i == '.':
        break
if stack:
    print('no')
else:
    print('yes')
print(stack)