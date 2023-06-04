# def solution(s):
#     answer, s = -1, list(s)
#     while s:
#         flag = False
#         for i in range(len(s)-1):
#             if s[i] == s[i+1]:
#                 s[i:i+2] = ''
#                 flag = True
#                 break
#         if not flag: break
    
#     return 0 if len(s) else 1


# solution('cdcd')

# def solution(s):
#     s = list(s)
#     while s:
#         stack, flag = [], False
#         for i,idx in enumerate(range(len(s)-1)):
#             if flag:
#                 flag = False
#                 continue
#             if s[i] != s[i+1]:
#                 if idx != len(s)-2: 
#                     stack.append(s[i])
#                 else:
#                     stack.append(s[i])
#                     stack.append(s[i+1])
                
#             else: flag = True
#         if len(stack) == 0 or len(s) == len(stack): break
#         s = stack
        
#     return 0 if len(stack) else 1

# solution('cdcd')



def solution(s):
    stack = []
    for i in s:
        if not stack: stack.append(i)
        else:
            if stack[-1] == i: stack.pop()
            else: stack.append(i)
    return 0 if len(stack) else 1
