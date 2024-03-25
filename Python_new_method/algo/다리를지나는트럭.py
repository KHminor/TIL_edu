from collections import deque
def solution(bridge_length, weight, truck_weights):
    result,now,cnt = 0,0,0
    q = deque([])

    for t in truck_weights:
        if weight < now+t: 
            # result += len(q)
            while q: result += bridge_length - q.popleft()
            # q.clear()
            now,cnt = 0,0
        q.append(cnt)
        now += t
        cnt += 1
        # print(t,q,now,result)

    return result+bridge_length+len(q)


print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))

r = 7+1
cnt = 1
q = [[6,0]]