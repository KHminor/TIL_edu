# from collections import deque
# def solution(bridge_length, weight, truck_weights):
#     result,now,cnt = 0,0,0
#     q = deque([])

#     for t in truck_weights:
#         if weight < now+t: 
#             while q: result += bridge_length - q.popleft()
#             now,cnt = 0,0
#         q.append(cnt)
#         now += t
#         cnt += 1
#     return result+bridge_length+len(q)


from collections import deque
def solution(bridge_length, weight, truck_weights):
    result,now,cnt = 0,0,0
    b_num = truck_weights[-1]
    q = deque([])

    for t in truck_weights:
        if weight < now+t: 
            result += len(q)
            q.clear()
            now,cnt = 0,0

        q.append(cnt)
        if t != b_num:
            now += t
            cnt += 1
            result += 1
    return result+bridge_length+len(q)

print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))

now = 0
q = [0]
r = 6
