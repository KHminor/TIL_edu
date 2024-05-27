# def solution(n, left, right):
#     cnt, li, flag = 0, [], False
#     for i in range(n):
#         if left > cnt + n: 
#             cnt += n
#             continue
#         for j in range(n):
#             if left <= cnt <= right:
#                 x = 0 # 해당 칸의 값
#                 if i >= j: x = i
#                 else: x = j
#                 li = li + [x+1]
#             elif cnt > right: 
#                 flag = True
#                 break
#             cnt += 1
#         if flag == True: break
#     return li

def solution(n, left, right):
    result = []
    for i in range(left, right+1):
        x, y = i//n, i%n
        if x >= y: result.append(x+1)
        else: result.append(y+1)    
    return result


solution(3, 2, 5)