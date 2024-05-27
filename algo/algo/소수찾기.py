# def solution(n):
#     result = [2]
#     for i in range(3,n+1):
#         state = True
#         rng = round(i**(1/2))
#         for j in range(2,rng+1):
#             if not i%j:
#                 state = False
#                 break
#         if state: result.append(i)
#     return len(result)


def solution(n):
    li = [1]*(n+1)
    for i in range(2,n+1):
        if li[i] != 0:
            for j in range(2*i,n+1,i): li[j] = 0
    return sum(li[2:])


print(solution(10))
print(solution(5))