import heapq

def solution(k, score):
    result = [0]*len(score)
    li = [-1]*k
    num = 20000
    heapq.heapify(li)
    for i in range(len(score)):
        if score[i] >= li[0]:
            num = min(num, score[i]) 
            heapq.heappop(li)
            heapq.heappush(li,score[i]) 
        if k > i: result[i] = num
        else: result[i] = li[0]
    return result

print(solution(8,[10, 100, 20, 150, 1, 100, 200]))
print(solution(3,[10, 100, 20, 150, 1, 100, 200]))
# print(solution(3,[30, 100, 20, 150, 1, 100, 100, 100, 200]))
# print(solution(4,[0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]	))