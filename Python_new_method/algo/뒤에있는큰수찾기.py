# def solution(numbers):
#     result = [0]*len(numbers)
#     mx = max(numbers)
#     for i,a in enumerate(numbers):
#         state = True
#         if a != mx:
#             for j in range(i+1, len(numbers)):
#                 if numbers[j] > a:
#                     state = False 
#                     result[i] = numbers[j]
#                     break
#         if state: result[i] = -1
#     return result

def solution(numbers):
    result = [0]*len(numbers)
    result[-1] = -1
    mx = numbers[-1]
    for i in range(len(numbers)-2,-1,-1):
        state = True
        if mx > numbers[i]:
            for j in range(i+1,len(numbers)):
                if numbers[j] > numbers[i]:
                    state = False
                    result[i] = numbers[j]
                    break
        if state: 
            mx = numbers[i]
            result[i] = -1
    return result



from collections import deque

def solution(numbers):
    result = [-1]*len(numbers)
    q = deque([(numbers[0],0)])
    for i,n in enumerate(numbers[1:]):
        while q and q[0][0]<n:
            _,idx = q.popleft()
            result[idx] = n
        q.appendleft((n,i+1))
    return result

# print(solution([2, 3, 3, 5]))
print(solution([9, 1, 5, 9, 3, 6, 2]))