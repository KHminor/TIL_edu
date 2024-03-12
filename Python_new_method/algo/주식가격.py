def solution(prices):
    result = [i for i in range(len(prices)-1,-1,-1)]
    for i in range(len(prices)):
        cnt = 1
        for j in range(i+1,len(prices)):
            if prices[i] > prices[j]: 
                result[i] = cnt
                break
            else: cnt += 1
    return result

def solution(prices):
    result = [i for i in range(len(prices)-1,-1,-1)]
    stack = []
    for i,p in enumerate(prices):
        if stack:
            while stack and stack[-1][1] > p:
                idx,_ = stack.pop()
                result[idx] -= result[i]
        stack.append([i,p])
    return result

print(solution([1,2,3,2,3]))
print(solution([1,2,3,4,3,2,3]))

[[0,1],[1,2],[2,3]]
[3,4]
past,_ = 3,4