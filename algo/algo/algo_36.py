def solution(n):
    li, result = [], 0
    while n != 0:
        li = li + [n%3]
        n = n//3
    li.reverse()
    for i in range(len(li)): 
        result += (3**i)*li[i]
    return result


def solution(n):
    s = ''
    while n != 0:
        s += str(n%3)
        n = n//3
    return int(s,3)

# def solution(n):
#     tmp = ''
#     while n:
#         tmp += str(n % 3)
#         n = n // 3

#     answer = int(tmp, 3)
#     return answer


print(solution(125))